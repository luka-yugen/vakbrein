#!/usr/bin/env python3
"""Mechanische controle van een vakbrein: links, weespagina's, index.

Gebruik:  python3 nakijken.py [hoofdmap van het brein]      (standaard: huidige map)
          python3 nakijken.py --selftest
Geeft een rapport in markdown. Past niets aan.

Wat het vindt:
  nog te schrijven   [[links]] naar pagina's die niet bestaan, meest genoemd eerst
  weespagina's       pagina's in Brain/ waar niets naar linkt
  niet in de index   pagina's in Brain/ die index.md niet noemt
Inhoudelijke controle (tegenspraak, verouderde stof) doet het model zelf, zie SCHEMA.md.
"""
import re, shutil, sys, tempfile
from collections import Counter
from pathlib import Path

LINK = re.compile(r"\[\[([^\]|#\\]+)")
CODE = re.compile(r"```.*?```|(`+)[^\n]*?\1", re.S)  # voorbeelden in code tellen niet
VAST = {"index", "log", "SCHEMA"}


def pages(root):
    return {p for p in root.rglob("*.md")
            if not any(x.startswith((".", "_")) for x in p.relative_to(root).parts)
            and "00 Bronnen" not in p.parts}


def rapport(root):
    root = Path(root)
    brain = root / "Brain"
    assert brain.is_dir(), f"geen Brain/ in {root}"
    alle = pages(root)
    namen = {p.stem for p in alle}
    brein = {p for p in alle if brain in p.parents}
    inkomend, ontbreekt = Counter(), Counter()
    for p in alle:
        for doel in set(l.strip() for l in LINK.findall(CODE.sub("", p.read_text(encoding="utf-8")))):
            doel = Path(doel).stem if doel.endswith(".md") else doel
            if doel in namen:
                if doel != p.stem:
                    inkomend[doel] += 1
            else:
                ontbreekt[doel] += 1
    index = brain / "index.md"
    in_index = set(LINK.findall(index.read_text(encoding="utf-8"))) if index.exists() else set()
    wees = sorted(p.stem for p in brein if p.stem not in VAST and not inkomend[p.stem])
    buiten = sorted(p.stem for p in brein if p.stem not in VAST and p.stem not in in_index)

    uit = [f"# Nakijken, {len(brein)} pagina's in Brain/", ""]
    uit += [f"## Nog te schrijven ({len(ontbreekt)})", ""]
    uit += [f"- [[{d}]], {n}x genoemd" for d, n in ontbreekt.most_common()] or ["niets"]
    uit += ["", f"## Weespagina's ({len(wees)})", ""] + ([f"- [[{w}]]" for w in wees] or ["geen"])
    uit += ["", f"## Niet in de index ({len(buiten)})", ""] + ([f"- [[{b}]]" for b in buiten] or ["alles staat erin"])
    if not index.exists():
        uit += ["", "Let op: Brain/index.md bestaat niet."]
    return "\n".join(uit) + "\n", ontbreekt, wees, buiten


def selftest():
    d = Path(tempfile.mkdtemp())
    (d / "Brain/Concepts").mkdir(parents=True)
    (d / "00 Bronnen").mkdir()
    (d / "Brain/index.md").write_text("[[Dwaling]] [[log]]")
    (d / "Brain/log.md").write_text("")
    (d / "Brain/Concepts/Dwaling.md").write_text("zie [[Bedrog|bedrog]] en [[Nietigheid#relatief]] en [[Dwaling]]")
    (d / "Brain/Concepts/Nietigheid.md").write_text("tabel: [[Dwaling\\|dwaling]]")
    (d / "Brain/Concepts/Wees.md").write_text("[[Bedrog]] `[[Voorbeeld]]` ``[[Dubbel]]``\n```\n[[Ook niet]]\n```")
    (d / "00 Bronnen/bron.md").write_text("[[Genegeerd]]")
    _, ontbreekt, wees, buiten = rapport(d)
    assert ontbreekt == {"Bedrog": 2}, ontbreekt
    assert wees == ["Wees"], wees
    assert buiten == ["Nietigheid", "Wees"], buiten
    shutil.rmtree(d)
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    else:
        print(rapport(sys.argv[1] if len(sys.argv) > 1 else ".")[0])
