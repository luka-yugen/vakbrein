---
name: vakbrein
description: Bouwt en onderhoudt een studiebrein voor één vak volgens Karpathy's LLM Wiki-methode. De student zet al het vakmateriaal (slides, lestranscripties, samenvattingen, oefeningen, oude examens, Kami-pdf's met notities) in een map, en de skill maakt er een gelinkte markdown-wiki van met examensignalen, een examenmodus en een studiepagina in HTML. Use when the user wants a study brain or second brain for a course, or says "vakbrein", "maak een brein voor dit vak", "verwerk deze les", "nieuw materiaal", "kijk mijn brein na", "overhoor me", "examen oefenen", "maak de examenstof".
---

# Vakbrein

Eén vak, één map, één brein. De student levert materiaal en stelt vragen. Jij doet het
boekhoudwerk: samenvatten, verbinden, opbergen, controleren. De methode is Karpathy's
[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): ruwe bronnen
die niemand aanraakt, een wiki die jij schrijft, en een schema met de regels.

Het brein dat je bouwt is zelfstandig. Het heeft een `AGENTS.md` die elke AI leest, een
`CLAUDE.md` die daarnaar verwijst, zijn eigen `Brain/SCHEMA.md` en de scripts in `_tools/`.
Na de bouw werkt het ook zonder deze skill.

`<skill>` hieronder is de map van dit bestand.

## Modi

De student noemt de modus (`/vakbrein nieuw`) of zegt gewoon wat er moet gebeuren.

| modus | wanneer | wat je leest |
|---|---|---|
| `nieuw` | een map met materiaal, nog geen `Brain/` | `<skill>/references/bouwen.md`, volledig |
| `ingest <bestand>` | het brein bestaat, er komt materiaal bij | "Ingest" in `Brain/SCHEMA.md` van het brein |
| `nakijken` | gaten, tegenspraak, dode links zoeken | "Nakijken" in `Brain/SCHEMA.md` |
| `examen` | de student wil zich testen | "Examen" in `Brain/SCHEMA.md` |
| `studielaag` | de studiepagina maken of bijwerken | `<skill>/references/studielaag.md` |

Geen modus genoemd: kijk of er een `Brain/SCHEMA.md` is in de huidige map of de map die de
student noemt. Nee: `nieuw`. Ja: leid de modus af uit wat de student zegt ("hier is les 9"
is `ingest`, "overhoor me over hoofdstuk 3" is `examen`), of vraag het.

Bij `ingest`, `nakijken` en `examen` volg je het SCHEMA.md van het brein zelf, niet een
kopie uit deze skill. De student of een vorige sessie kan het voor dit vak aangepast hebben.

Een brein van voor deze skill (zonder `_tools/`): kopieer `<skill>/scripts/*.py` naar
`_tools/` voor je begint.

## Wat altijd geldt

- **`00 Bronnen/` is onaanraakbaar.** Lezen, nooit bewerken. Bestanden verplaatsen alleen
  na akkoord.
- **Gericht op het examen van dit vak.** Elke pagina helpt de student een vraag in de echte
  examenvorm op te lossen. Lees `Brain/Het examen.md` als je twijfelt wat dat betekent.
- **Transcripties bevatten fouten.** Nooit een naam, getal, artikel of paginanummer uit een
  transcriptie overnemen zonder het tegen de slides of een andere bron te leggen.
- **De docent gaat voor.** Bij tegenspraak: wat de docent zei, dan slides en cursus, dan
  officiële examenregels, dan de notities van de student, dan samenvattingen van anderen.
  De volledige rangorde staat in `references/schema.md`.
- **Alles komt uit de bronnen.** Vul je iets aan uit algemene kennis, zeg dat erbij.
- **Log alles** in `Brain/log.md`. Zo kan een volgende sessie verder waar deze stopte.
- **Geen git zonder akkoord.** Bied het aan, doe het niet vanzelf, push nooit naar een
  publieke repo: er staat materiaal van de docent in.
- **Schrijfstijl.** Gewone taal, korte zinnen, de taal van het materiaal. Geen em dash, geen
  opvulzinnen, geen slotalinea die herhaalt wat er al stond. Is er een schrijfstijl-skill in
  deze omgeving, volg die.

## Scripts

Alle drie Python 3.9+, alleen standaardbibliotheek tenzij vermeld. Elk heeft `--selftest`.

| script | doet | vereist |
|---|---|---|
| `extract.py [map]` | pptx, docx, xlsx en pdf naar markdown in `<map>/_tekst/`, meldt scans en oude formaten | pdf: `pypdf` of `pdftotext` |
| `notities.py <pdf>...` | getypte notities, markeringen en doorhalingen uit een Kami-export | `pymupdf` |
| `nakijken.py [map]` | dode links, weespagina's en pagina's die niet in de index staan | niets |

Ontbreekt een vereiste, zeg welk commando het installeert en ga door met wat wel kan.
