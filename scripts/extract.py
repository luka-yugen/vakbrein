#!/usr/bin/env python3
"""Zet elk bronbestand (.pptx/.docx/.xlsx/.pdf) om in platte tekst onder <map>/_tekst/.

Gebruik:  python3 extract.py ["00 Bronnen"]
          python3 extract.py --selftest
Idempotent: bestaande output wordt overschreven. .md en .txt worden niet omgezet,
die lees je rechtstreeks.

pptx, docx en xlsx gaan zonder libraries: het zijn zipbestanden met XML.
pdf gebruikt pypdf als dat er is, anders pdftotext (poppler).
ponytail: geen ondersteuning voor de oude binaire formaten .ppt/.doc/.xls. Die worden
gemeld; zet ze om met  soffice --headless --convert-to pptx <bestand>  (of docx/xlsx).
"""
import re, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
S = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PR = "{http://schemas.openxmlformats.org/package/2006/relationships}"
OUD = {".ppt": "pptx", ".doc": "docx", ".xls": "xlsx"}
LEEG = 40  # minder tekens dan dit op een pdf-pagina: waarschijnlijk een scan


def a_text(blob):
    """Alle <a:t>-tekst, per <a:p> op een eigen regel."""
    lines = []
    for p in ET.fromstring(blob).iter(A + "p"):
        t = "".join(n.text or "" for n in p.iter(A + "t")).strip()
        if t:
            lines.append(t)
    return lines


def pptx(path):
    z = zipfile.ZipFile(path)
    names = set(z.namelist())
    nums = sorted(int(m.group(1)) for n in names
                  for m in [re.match(r"ppt/slides/slide(\d+)\.xml$", n)] if m)
    out = [f"# {path.stem}", f"_bron: {path.name}, {len(nums)} slides_", ""]
    for i in nums:
        out.append(f"\n## slide {i}")
        out += a_text(z.read(f"ppt/slides/slide{i}.xml"))
        note = f"ppt/notesSlides/notesSlide{i}.xml"
        if note in names:
            n = [l for l in a_text(z.read(note)) if l != str(i)]
            if n:
                out += ["\n### sprekersnotities"] + n
    return "\n".join(out)


def w_text(el):
    return "".join(t.text or "" for t in el.iter(W + "t")).strip()


def docx(path):
    """Paragrafen en tabellen in leesvolgorde. Koppen (Heading1, Kop1, ...) krijgen #."""
    body = ET.fromstring(zipfile.ZipFile(path).read("word/document.xml")).find(W + "body")
    out = [f"# {path.stem}", f"_bron: {path.name}_", ""]
    for el in body:
        if el.tag == W + "p":
            t = w_text(el)
            if not t:
                continue
            st = el.find(f"{W}pPr/{W}pStyle")
            m = re.search(r"(?:Heading|Kop|berschrift|Titre)\s*(\d)", st.get(W + "val", "") if st is not None else "")
            img = "[AFBEELDING] " if el.find(f".//{W}drawing") is not None else ""
            out.append(("\n" + "#" * (int(m.group(1)) + 1) + " " if m else "") + img + t)
        elif el.tag == W + "tbl":
            rows = [" | ".join(w_text(c).replace("\n", " / ") for c in tr.iter(W + "tc"))
                    for tr in el.iter(W + "tr")]
            out.append("\n[TABEL]\n" + "\n".join(rows) + "\n[/TABEL]")
    return "\n".join(out)


def xlsx(path):
    """Elk tabblad als rijen 'A1: waarde'. Formules staan erachter, voor rekenvakken is dat de leerstof."""
    z = zipfile.ZipFile(path)
    names = set(z.namelist())
    shared = []
    if "xl/sharedStrings.xml" in names:
        shared = ["".join(t.text or "" for t in si.iter(S + "t"))
                  for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(S + "si")]
    rels = {r.get("Id"): r.get("Target") for r in
            ET.fromstring(z.read("xl/_rels/workbook.xml.rels")).iter(PR + "Relationship")}
    out = [f"# {path.stem}", f"_bron: {path.name}_", ""]
    for sh in ET.fromstring(z.read("xl/workbook.xml")).iter(S + "sheet"):
        target = rels[sh.get(R + "id")].lstrip("/")
        target = target if target.startswith("xl/") else "xl/" + target
        out.append(f"\n## tabblad {sh.get('name')}")
        for row in ET.fromstring(z.read(target)).iter(S + "row"):
            cells = []
            for c in row.iter(S + "c"):
                v, f = c.find(S + "v"), c.find(S + "f")
                if c.get("t") == "inlineStr":
                    val = "".join(t.text or "" for t in c.iter(S + "t"))
                elif v is None:
                    val = ""
                elif c.get("t") == "s":
                    val = shared[int(v.text)]
                else:
                    val = v.text or ""
                if f is not None and f.text:
                    val += f"  (={f.text})"
                if val.strip():
                    cells.append(f"{c.get('r')}: {val.strip()}")
            if cells:
                out.append(" | ".join(cells))
    return "\n".join(out)


def pdf(path):
    try:
        import pypdf
        pages = [(pg.extract_text() or "") for pg in pypdf.PdfReader(path).pages]
    except ImportError:
        if not shutil.which("pdftotext"):
            raise RuntimeError("geen pdf-lezer: pip install pypdf  of installeer poppler (pdftotext)")
        raw = subprocess.run(["pdftotext", "-layout", str(path), "-"],
                             capture_output=True, text=True, check=True).stdout
        pages = raw.split("\f")[:-1] or [raw]
    out = [f"# {path.stem}", f"_bron: {path.name}, {len(pages)} pagina's_", ""]
    for i, t in enumerate(pages, 1):
        t = t.strip()
        flag = "\n[WEINIG OF GEEN TEKST: waarschijnlijk een scan of afbeelding, open de pagina zelf]" if len(t) < LEEG else ""
        out.append(f"\n## pagina {i}{flag}\n{t}")
    return "\n".join(out)


READERS = {".pptx": pptx, ".docx": docx, ".xlsx": xlsx, ".pdf": pdf}


def run(src):
    src = Path(src)
    assert src.is_dir(), f"map bestaat niet: {src}"
    out_dir = src / "_tekst"
    files = sorted(p for p in src.rglob("*") if p.is_file()
                   and "_tekst" not in p.relative_to(src).parts
                   and not any(x.startswith(".") for x in p.relative_to(src).parts))
    fouten = 0
    for p in files:
        ext = p.suffix.lower()
        if ext in OUD:
            print(f"OUD FORMAAT  {p.name}: soffice --headless --convert-to {OUD[ext]} \"{p}\"", file=sys.stderr)
            fouten += 1
            continue
        if ext not in READERS:
            continue
        dest = out_dir / p.relative_to(src).with_suffix(".md")
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            text = READERS[ext](p)
        except Exception as e:
            print(f"FOUT  {p.name}: {e}", file=sys.stderr)
            fouten += 1
            continue
        dest.write_text(text, encoding="utf-8")
        scans = text.count("[WEINIG OF GEEN TEKST")
        print(f"{len(text):8d} tekens  {dest.relative_to(src)}" + (f"  ({scans} pagina's zonder tekst)" if scans else ""))
    return fouten


def selftest():
    """Bouwt een mini-pptx, -docx en -xlsx en controleert of de tekst eruit komt."""
    d = Path(tempfile.mkdtemp())
    a, w, s = A[1:-1], W[1:-1], S[1:-1]
    r = R[1:-1]
    with zipfile.ZipFile(d / "les.pptx", "w") as z:
        z.writestr("ppt/slides/slide2.xml", f'<p:sld xmlns:p="x" xmlns:a="{a}"><a:p><a:r><a:t>Tweede slide</a:t></a:r></a:p></p:sld>')
        z.writestr("ppt/slides/slide1.xml", f'<p:sld xmlns:p="x" xmlns:a="{a}"><a:p><a:r><a:t>Dwaling</a:t></a:r><a:r><a:t> is</a:t></a:r></a:p></p:sld>')
        z.writestr("ppt/notesSlides/notesSlide1.xml", f'<p:notes xmlns:p="x" xmlns:a="{a}"><a:p><a:r><a:t>komt op examen</a:t></a:r></a:p><a:p><a:r><a:t>1</a:t></a:r></a:p></p:notes>')
    with zipfile.ZipFile(d / "sv.docx", "w") as z:
        z.writestr("word/document.xml", f'<w:document xmlns:w="{w}"><w:body>'
                   '<w:p><w:pPr><w:pStyle w:val="Kop1"/></w:pPr><w:r><w:t>Hoofdstuk een</w:t></w:r></w:p>'
                   '<w:p><w:r><w:t>Gewone </w:t></w:r><w:r><w:t>tekst</w:t></w:r></w:p>'
                   '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>a</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>b</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
                   '</w:body></w:document>')
    with zipfile.ZipFile(d / "oef.xlsx", "w") as z:
        z.writestr("xl/workbook.xml", f'<workbook xmlns="{s}" xmlns:r="{r}"><sheets><sheet name="KVS" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels", f'<Relationships xmlns="{PR[1:-1]}"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr("xl/sharedStrings.xml", f'<sst xmlns="{s}"><si><t>Totaal</t></si></sst>')
        z.writestr("xl/worksheets/sheet1.xml", f'<worksheet xmlns="{s}"><sheetData><row r="1">'
                   '<c r="A1" t="s"><v>0</v></c><c r="B1"><f>SUM(C1:C2)</f><v>42</v></c></row></sheetData></worksheet>')
    (d / "oud.ppt").write_bytes(b"x")
    (d / ".verborgen.docx").write_bytes(b"x")

    assert run(d) == 1, "oud.ppt moet als 1 fout gemeld worden, .verborgen overgeslagen"
    p = (d / "_tekst/les.md").read_text()
    assert "Dwaling is" in p and p.index("slide 1") < p.index("slide 2"), p
    assert "komt op examen" in p and "\n1\n" not in p, p
    t = (d / "_tekst/sv.md").read_text()
    assert "## Hoofdstuk een" in t and "Gewone tekst" in t and "a | b" in t, t
    x = (d / "_tekst/oef.md").read_text()
    assert "## tabblad KVS" in x and "A1: Totaal" in x and "B1: 42  (=SUM(C1:C2))" in x, x
    assert run(d) == 1, "tweede run moet hetzelfde geven (idempotent)"
    shutil.rmtree(d)
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    else:
        sys.exit(1 if run(sys.argv[1] if len(sys.argv) > 1 else "00 Bronnen") else 0)
