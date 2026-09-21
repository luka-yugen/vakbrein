#!/usr/bin/env python3
"""Haal je eigen annotaties uit een pdf die je uit Kami exporteerde.

Wat eruit komt, per pagina: getypte notities, markeringen (per kleur, met de woorden
eronder), doorhalingen, en of er met de hand pijlen of lijnen getekend zijn.
Zo zie je waar je tijdens de les de nadruk legde.

Gebruik:  python3 notities.py <pdf> [pdf ...]     schrijft <naam>_notities.md naast de pdf
          python3 notities.py --selftest
Vereist PyMuPDF:  pip install pymupdf

Kami zet getypte notities in Roboto met kleur #0066cc (of #ff0000). Een slidetemplate
kan ook Roboto gebruiken, maar dan in een andere kleur, dus de kleur is het onderscheid.
ponytail: kleurherkenning in plaats van een diff met de blanco versie. Andere annotatie-app
of ander palet? Draai dan een tekst-diff tegen _tekst/ van de blanco pdf.
Beperking: handgetekende pijlen komen er alleen als kleur uit, niet als vorm. Bij twijfel
de pagina als afbeelding openen.
"""
import sys, pathlib

NOTITIE_KLEUR = {0x0066cc, 0xff0000}
KLEUR = {(0, 1, 0): "groen", (1, 1, 0): "geel", (0.95, 1, 0): "geel", (1, 0.78, 0): "oranje",
         (0, 1, 1): "cyaan", (1, 0, 1): "magenta", (1, 0, 0): "rood", (1, 0.4, 0.4): "rood",
         (0.6, 0.8, 1): "blauw"}


def naam(rgb):
    """RGB (0-1) naar een kleurnaam, of None voor wit, zwart en grijs."""
    if rgb is None:
        return None
    r, g, b = [round(c, 2) for c in rgb]
    if (r, g, b) in KLEUR:
        return KLEUR[(r, g, b)]
    if min(r, g, b) > .9 or max(r, g, b) < .15 or max(r, g, b) - min(r, g, b) < .1:
        return None
    best, dist = None, 9
    for k, v in KLEUR.items():
        d = sum((a - c) ** 2 for a, c in zip(k, (r, g, b)))
        if d < dist:
            best, dist = v, d
    return best if dist < .25 else None


def verwerk(pdf):
    import fitz
    doc = fitz.open(pdf)
    kop = [f"# {pathlib.Path(pdf).stem.replace('_NOTITIES', '')}", "", ""]
    uit, n_pag = [], 0
    for i, pag in enumerate(doc, 1):
        notities, woorden = [], []
        for blok in pag.get_text("dict")["blocks"]:
            for lijn in blok.get("lines", []):
                tekst = "".join(s["text"] for s in lijn["spans"]).strip()
                if not tekst:
                    continue
                if any(s["color"] in NOTITIE_KLEUR and s["font"].startswith("Roboto") for s in lijn["spans"]):
                    notities.append(tekst)
                    continue
                for s in lijn["spans"]:
                    for w in pag.get_text("words", clip=fitz.Rect(s["bbox"])):
                        woorden.append((fitz.Rect(w[:4]), w[4]))

        tekeningen = pag.get_drawings()
        markering, streep, inkt = {}, {}, set()
        for d in tekeningen:
            r = d["rect"]
            k = naam(d.get("fill"))
            if k:
                if 5 < r.width and 4 < r.height < 90:
                    raak = [t for bb, t in woorden if abs(bb & r) > .3 * abs(bb)]
                    if raak:
                        markering.setdefault(k, []).extend(raak)
                continue
            k = naam(d.get("color"))
            if not k or d.get("fill"):
                continue
            if r.height < 25 and r.width > 40:  # vlakke haal over tekst
                raak = [t for bb, t in woorden if abs(bb & r) > .3 * abs(bb)]
                if raak:
                    streep.setdefault(k, []).extend(raak)
                    continue
            inkt.add(k)

        if not (notities or markering or streep):
            continue
        n_pag += 1
        uit.append(f"\n## p{i}")
        if notities:
            uit.append("notitie: " + " · ".join(notities))
        for k, v in markering.items():
            uit.append(f"markering {k}: " + " ".join(dict.fromkeys(v)))
        for k, v in streep.items():
            uit.append(f"doorstreept ({k}): " + " ".join(dict.fromkeys(v)))
        if inkt:
            uit.append(f"_pijl of lijn getekend: {', '.join(sorted(inkt))}_")
    kop[1] = f"_{n_pag} van {len(doc)} pagina's geannoteerd_"
    return "\n".join(kop + uit) + "\n"


def selftest():
    assert naam((1, 1, 0)) == "geel"
    assert naam((0.98, 0.97, 0.1)) == "geel", "bijna-geel moet geel blijven"
    assert naam((1, 1, 1)) is None and naam((0, 0, 0)) is None, "wit en zwart zijn geen markering"
    assert naam((0.5, 0.5, 0.5)) is None, "grijs is geen markering"
    assert naam(None) is None
    assert naam((0.2, 0.3, 0.9)) is None, "UGent-blauw of een ander ver blauw is geen markering"
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
        sys.exit()
    assert len(sys.argv) > 1, "gebruik: notities.py <pdf> [pdf ...]"
    try:
        import fitz  # noqa: F401
    except ImportError:
        sys.exit("PyMuPDF ontbreekt: pip install pymupdf")
    for f in sys.argv[1:]:
        p = pathlib.Path(f)
        dest = p.parent / (p.stem.replace("_NOTITIES", "") + "_notities.md")
        t = verwerk(f)
        dest.write_text(t, encoding="utf-8")
        print(f"{len(t):7d} tekens  {dest.name}")
