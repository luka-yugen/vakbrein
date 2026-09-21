# Een nieuw vakbrein bouwen

Volg de stappen in volgorde. Sla er geen over, ook niet als het materiaal klein is.
`<skill>` is de map waar dit bestand in `references/` staat.

## 1. De map vaststellen

Het brein komt in de map waar het materiaal staat, of in de map die de student noemt.
Zoek de hoofdmap van het vak, niet een submap met alleen slides.

Het ruwe materiaal moet in `00 Bronnen/` zitten. Ligt het los in de hoofdmap:
stel voor om het naar `00 Bronnen/` te verplaatsen en wacht op akkoord. Verplaats nooit
zonder te vragen. Zeg "nee", laat het dan staan en behandel de hoofdmap als bronnenmap
(schrijf dat in AGENTS.md).

Bestaat er al een `Brain/SCHEMA.md`? Dan is dit geen nieuw brein. Stop en zeg dat
`ingest` of `nakijken` de bedoeling is.

## 2. Inventaris

Maak een lijst van elk bestand in `00 Bronnen/`: naam, type, grootte. Deel elk bestand in
één soort in:

| soort | herken je aan |
|---|---|
| slides | pptx, pdf met "les", "hoofdstuk", "module", slidenummers |
| transcriptie | .md of .txt met gesproken taal, "euh", tijdstempels, datums in de naam |
| cursus of handboek | lange pdf met hoofdstukken, ISBN |
| eigen samenvatting | naam van de student, "samenvatting", "sv", eigen docx |
| samenvatting van anderen | Stuvia, Knoowy, naam van een andere student, "oplossingen alle oefeningen" |
| geannoteerde pdf | "Kami Export" in de naam, gekleurde markeringen |
| opgaven en oefeningen | xlsx, "oefening", "opgave", "case" |
| oplossingen | "oplossing", "modeloplossing", "correctiesleutel" |
| oude examens en voorbeeldvragen | "examen", "proef", "voorbeeldvragen", een jaartal |
| examenregels en praktisch | "examenrichtlijnen", "leerstof proeven", "planning", tekenlijst |
| overig | alles wat nergens past, noem het apart |

Tekenlijsten en klaslijsten bevatten namen van andere studenten. Lees ze niet verder dan
nodig om te weten wat ze zijn, en neem geen namen over in het brein.

## 3. Extractie

```bash
mkdir -p _tools && cp <skill>/scripts/*.py _tools/
python3 _tools/extract.py "00 Bronnen"
```

Dat zet pptx, docx, xlsx en pdf om naar markdown in `00 Bronnen/_tekst/`. De scripts gaan
mee in `_tools/`, zodat het brein later ook zonder deze skill bij te werken is.

Wat het script meldt, los je zo op:

- **OUD FORMAAT** (.ppt, .doc, .xls). Staat LibreOffice er (`soffice`), zet ze om naar
  `00 Bronnen/_omgezet/` met `soffice --headless --convert-to pptx --outdir "00 Bronnen/_omgezet" <bestand>`
  en draai extract.py opnieuw. Geen LibreOffice: noteer het bestand als gat.
- **Pagina's zonder tekst**: scans of afbeeldingen. Kan je afbeeldingen lezen, open die
  pagina's en lees ze. Anders: noteer ze als gat.
- **FOUT**: noteer het bestand en ga door. Eén kapot bestand houdt de bouw niet tegen.

Geannoteerde pdf's uit Kami:

```bash
python3 _tools/notities.py "00 Bronnen/<bestand>.pdf"
```

Dat geeft `<bestand>_notities.md` met de getypte notities, markeringen en doorhalingen van
de student per pagina. Die wegen zwaar: wat de student markeerde is wat de docent benadrukte.
Komt de pdf uit een andere app en geeft het script niets, zeg dat en lees de pdf zelf.

## 4. De interviewronde

Eén ronde, maximaal vijf vragen. Heb je een tool om vragen met keuzes te stellen, gebruik
die. Anders één bericht met genummerde vragen. Geef bij elke vraag je voorstel, afgeleid
uit het materiaal, zodat de student alleen hoeft te bevestigen.

1. **Vak en docent.** Naam en code van het vak, opleiding, instelling, docent(en).
   Meestal staat dit op de eerste slide.
2. **Examenvorm.** Meerkeuze met stellingen, open vragen, oefeningen, mondeling, of een mix.
   Hoeveel vragen, hoeveel tijd, cijferregels (gisstraf, cesuur). Zoek eerst in examenregels
   en oude examens.
3. **Datum en hulpmiddelen.** Wanneer is het examen, wat mag mee (codex, rekenmachine,
   formularium, niets).
4. **Vaktype.** Theorie, rekenen of gemengd. Zie stap 5 voor wat dat verandert. Stel voor op
   basis van de inventaris: veel xlsx, oplossingen en cases is rekenen, veel begrippen en
   wetten is theorie.
5. **Bronnen van anderen.** Welke samenvattingen komen van andere studenten of betaalde sites,
   en welke is van de student zelf. Bevestig wat je in de inventaris aanduidde.

Wat de student openlaat, vul je in met je voorstel. Zet het in AGENTS.md onder
"Openstaande punten" met "(aangenomen)" erachter.

De taal van het brein is de taal van het materiaal, tenzij de student iets anders zegt.

## 5. De structuur zetten

Altijd:

```
<vak>/
  AGENTS.md             de instructies voor elke AI (zie stap 7)
  CLAUDE.md             één regel: @AGENTS.md
  00 Bronnen/           ruw, onaanraakbaar
  _tools/               de scripts
  Brain/
    SCHEMA.md           uit <skill>/references/schema.md, ingevuld
    index.md
    log.md
    Het examen.md       vorm, hulpmiddelen, cijfers, praktisch
    Examensignalen.md   alles wat de docent over het examen zei
    Topics/             de delen van de cursus, als hubs
    Lessen/             één notitie per college
    Concepts/           begrippen, leerstukken, methodes
```

Per vaktype komt erbij:

| vaktype | extra | het rijke knooppunt |
|---|---|---|
| theorie | `Entities/` voor wetten, artikelen, auteurs, modellen, instanties, arresten | Concepts |
| rekenen | `Oefeningen/` met één pagina per kernoefening, en `Formules.md` | Oefeningen |
| gemengd | beide | allebei |

Het rijke knooppunt is waar de meeste tekst en links naartoe gaan. Bij een rekenvak leert
de student door oefeningen te maken, dus daar zit de uitleg: in de oefening, met de methode
stap voor stap. De Concepts-pagina's blijven dan kort en wijzen naar de oefeningen.

Wat er ook bij kan, alleen als het materiaal het heeft:

- `Voorbeeldexamen.md` als de docent voorbeeldvragen gaf of uitwerkte.
- `Examen <maand jaar>.md` per oud examen, met per vraag het juiste antwoord en waarom.
- `Brug <naam samenvatting>.md` als de student een eigen samenvatting heeft: per hoofdstuk
  of paginabereik welke breinpagina erbij hoort, en waar de samenvatting fout of verouderd is.
- `Paginas.md` als lesopnames naar een oudere editie van het handboek verwijzen: de mapping
  van oude naar nieuwe paginanummers, gecontroleerd tegen de huidige slides.

## 6. Schrijven

Werk bron per bron. Schrijf na elke verwerkte bron een regel in `Brain/log.md`:

```
## [JJJJ-MM-DD] ingest | <bronbestand>
<een regel: welke pagina's je maakte of bijwerkte>
```

Zo kan een nieuwe sessie verder waar de vorige stopte: lees `log.md`, sla over wat erin
staat. Bij veel materiaal (tien lessen of meer) is dat geen luxe, een sessie kan halverwege
stoppen.

Kan je hulpagenten starten, dan mag elke agent een of enkele `Lessen/`-notities schrijven.
Concepts, Oefeningen en Topics schrijf je zelf, zodat ze één stem en één structuur hebben.

### Volgorde

1. **Lessen.** Eén notitie per college, uit transcriptie en slides samen. Geen transcripties?
   Dan één notitie per slidedeck of hoofdstuk.
2. **Concepts en Oefeningen.** Na alle lessen, zodat je per begrip alles bij elkaar hebt.
   Eén bron raakt vaak tien pagina's, dat hoort zo.
3. **Entities**, bij theorie en gemengd.
4. **Topics.** Volg de indeling van de cursus zelf: de slidedecks, de hoofdstukken of de
   modules. Niet je eigen indeling.
5. **Examensignalen.** Loop elke transcriptie en elke notitie na op uitspraken over het
   examen. Zoek op: examen, vragen, kennen, van buiten, belangrijk, niet kennen, komt,
   punten, leerstof, oefening, "dat moet je kunnen". Zet ze per leerstuk, met het citaat en
   de les waar het viel. Dit is de meest gebruikte pagina van het brein, besteed er tijd aan.
6. **Het examen**, en waar van toepassing Voorbeeldexamen, oude examens, Brug, Paginas.
7. **index.md.** Elke pagina met één regel uitleg. Bovenaan "Begin hier" met Examensignalen,
   Het examen en wat het meest helpt voor dit vak.

### Paginaformaten

Elke pagina begint met frontmatter en een kop. Wikilinks `[[Naam]]` op de plek waar ze
kloppen. Een link naar een pagina die nog niet bestaat is prima, dat is een to-do.

**Les** (`Lessen/2025-10-07.md`, of `Lessen/Les 03.md` als de datum onbekend is):

```markdown
---
type: les
datum: 2025-10-07
topic: "[[Overeenkomstenrecht]]"
bronnen: [transcripties/2025-10-07.md, slides/Overeenkomst.pptx]
---

# 2025-10-07, totstandkoming van de overeenkomst

Wat er behandeld werd, in een paar zinnen. Welke slides.

## Wat de docent benadrukte
Met citaat waar het helpt.

## Examensignalen
Letterlijk wat er over het examen gezegd werd. Staat ook in [[Examensignalen]].

## Pagina's
[[Aanbod en aanvaarding]] · [[Dwaling]]
```

**Concept** (`Concepts/Dwaling.md`):

```markdown
---
type: concept
topic: "[[Overeenkomstenrecht]]"
bronnen: [slides/Overeenkomst.pptx slide 34-41, les 2025-10-07]
---

# Dwaling

De kern in twee of drie zinnen, zo geformuleerd dat je er een examenvraag mee oplost.

Dan de uitleg, in secties die bij het begrip passen.

## Valkuilen op het examen
Waar een stelling of vraag je kan vangen.

## Zie ook
[[Bedrog]] · [[Nietigheid]]
```

**Oefening** (`Oefeningen/Lambourcia.md`):

```markdown
---
type: oefening
topic: "[[Full costing]]"
opgave: <bestand, pagina>
oplossing: <bestand, pagina, of "geen">
---

# Lambourcia

## Opgave in het kort
Wat gegeven is, wat gevraagd wordt.

## Methode stap voor stap
Genummerd. Bij elke stap de formule en het tussenresultaat.

## Uitkomst
De eindcijfers, zodat de student zichzelf kan controleren.

## Valkuilen
## Lijkt op
[[Spiessens]] · [[Kostenverdeelstaat]]
```

Controleer elk cijfer in een oplossing van een andere student zelf na. Wijkt het af, schrijf
je eigen uitkomst en zet erbij wat de bron zegt.

**Entity** (`Entities/Art. 5.72 BW.md`): frontmatter `type: entity` en `soort:` (wet, artikel,
persoon, instantie, model, boek, arrest), dan wat het is en waar het in het vak terugkomt.

**Topic** (`Topics/Overeenkomstenrecht.md`): frontmatter `type: topic`, dan een alinea over
dit deel, hoe zwaar het weegt op het examen (uit Examensignalen), en de lijst Lessen,
Concepts, Oefeningen en Entities die erbij horen.

### Schrijfstijl

Gewone taal, korte zinnen, gericht op wat er op het examen gebeurt. Niet "wat is dwaling",
wel "welk woord maakt deze stelling over dwaling fout". Geen em dash. Geen opvulzinnen en
geen slotalinea die samenvat wat er al stond. Is er in deze omgeving een schrijfstijl-skill,
volg die.

## 7. AGENTS.md, CLAUDE.md en SCHEMA.md

`Brain/SCHEMA.md`: kopieer `<skill>/references/schema.md`, vul de `{{...}}` in, schrap de
rijen voor paginatypes die dit brein niet heeft, en zet onder "Regels voor dit vak" wat je
tijdens het bouwen leerde (bv. "Boek 6 BW is nieuw sinds 2025, oudere bronnen kloppen niet").

`CLAUDE.md` in de hoofdmap is één regel:

```
@AGENTS.md
```

Claude Code leest CLAUDE.md, de meeste andere tools lezen AGENTS.md. Zo is er één bestand
om bij te houden.

`AGENTS.md` in de hoofdmap, volgens dit sjabloon. Hou het onder de 120 regels. Het is de
eerste tekst die elke AI leest, dus alleen wat telt.

```markdown
# <Vak>, brein

Map van <naam student>, <opleiding>, <instelling>.
Vak **<naam> (<code>)**, docent(en) <namen>. Examen <datum of periode>.

## Hoe deze map werkt

Dit is een LLM Wiki (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
Het ruwe materiaal staat in `00 Bronnen/` en wordt nooit bewerkt. De AI schrijft en
onderhoudt `Brain/`. De regels staan in `Brain/SCHEMA.md`, lees die voor je iets verwerkt.

<de mapstructuur van dit brein, zoals in stap 5, met aantallen pagina's>

## Wat je moet weten voor je iets zegt

<vijf tot tien regels. De examenvorm en wat dat betekent voor elk antwoord. Wat mee mag.
Welke bron voorgaat bij tegenspraak. Bekende fouten in transcripties of samenvattingen.
Alles wat een AI zonder deze kennis fout zou doen.>

## Wat je kan vragen

| zeg | wat er gebeurt |
|---|---|
| een vraag over de leerstof | antwoord uit het brein, met links naar de pagina's |
| "nieuw materiaal: <bestand>" | het bestand wordt verwerkt in het brein |
| "kijk het brein na" | controle op gaten, tegenspraak en dode links |
| "examen" | oefenexamen in de echte examenvorm, zwakke plekken worden bijgehouden |
| "maak de studielaag" | examenstof.html met planning en oefenvragen |

## Nieuw materiaal toevoegen

1. Zet het bestand in `00 Bronnen/`.
2. `python3 _tools/extract.py "00 Bronnen"`
3. Kami-pdf met notities: `python3 _tools/notities.py "00 Bronnen/<bestand>.pdf"`
4. Volg "Ingest" in `Brain/SCHEMA.md`.

## Openstaande punten

<gaten uit de bouw: scans die niet gelezen zijn, lessen zonder transcriptie, aannames uit de
interviewronde, tegenspraak die de student moet beslissen>
```

## 8. Eindcontrole

```bash
python3 _tools/nakijken.py .
```

Los op wat mechanisch is: pagina's die niet in de index staan, weespagina's die een link
verdienen. "Nog te schrijven" met drie of meer vermeldingen: schrijf die pagina's nu.
De rest mag als to-do blijven staan.

Controleer daarna zelf of elke Concept- en Oefeningpagina minstens één bron noemt, en of
Examensignalen gevuld is. Is er echt niets over het examen gezegd, zet dat er letterlijk in.

## 9. Opleveren

Vertel de student in een paar regels:

- hoeveel pagina's per soort er zijn, en welke bronnen verwerkt zijn
- wat er ontbreekt: scans, oude formaten, lessen zonder transcriptie, aannames
- wat de student nu kan doen: de tabel "Wat je kan vragen" uit AGENTS.md
- dat de map als vault in Obsidian opent, voor wie de grafiek wil zien

Bied dan git aan, zonder het zelf te doen:

> Wil je dit onder versiebeheer? Dan zie je elke wijziging die de AI maakt en kan je terug.
> Push je het naar een privé-repo op GitHub, dan werkt het brein ook in cloudsessies,
> bijvoorbeeld op je gsm via claude.ai/code.

Zegt de student ja: `git init`, een `.gitignore` met `.DS_Store` en `.obsidian/workspace*`,
en een eerste commit. Pushen alleen als de student de repo zelf aanmaakt of er uitdrukkelijk
om vraagt, en altijd privé: er staat materiaal van de docent in.

Schrijf ten slotte een regel `## [datum] bouw | brein aangemaakt` in `log.md`.
