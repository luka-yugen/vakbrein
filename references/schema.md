---
type: brain-schema
vak: {{VAK}} ({{CODE}}), {{OPLEIDING}}
vaktype: {{theorie|rekenen|gemengd}}
bijgewerkt: {{DATUM}}
---

# SCHEMA, hoe dit brein werkt

Dit is de regellaag van een [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f),
toegepast op één vak. Lees dit voor je een bron verwerkt, een vraag beantwoordt, het brein
nakijkt of een examen afneemt.

## Het patroon

Ruwe bronnen (onaanraakbaar) → de wiki (de AI schrijft en onderhoudt elke pagina) → dit schema.
De student levert materiaal aan en stelt vragen. De AI doet het boekhoudwerk: samenvatten,
verbinden, opbergen, controleren. Een goed antwoord verdwijnt niet in de chat, het wordt een
pagina.

## Drie lagen

1. **Ruwe bronnen** in `00 Bronnen/`. Lezen mag, bewerken nooit. `_tekst/` bevat de
   extractie, `*_notities.md` de eigen annotaties van de student.
2. **De wiki** onder `Brain/`, eigendom van de AI.
3. **Het schema**: dit bestand plus `AGENTS.md` in de hoofdmap.

## Paginatypes

| map | wat er staat |
|---|---|
| `Lessen/` | één notitie per college: datum, wat behandeld werd, wat de docent benadrukte |
| `Concepts/` | begrippen, leerstukken, methodes. Eén pagina per begrip, groeit mee |
| `Entities/` | wat buiten het vak bestaat: wetten, artikelen, auteurs, modellen, instanties |
| `Oefeningen/` | één pagina per kernoefening: opgave, methode stap voor stap, uitkomst, valkuilen |
| `Topics/` | de delen van de cursus, als hub naar de rest |

Een **entity** bestaat buiten dit vak. Een **concept** moet je kunnen uitleggen en toepassen.
Een **oefening** moet je kunnen maken. Een **topic** is een deel van de cursus.
Twijfel je, maak er een Concept van.

Vaste pagina's: `index.md` (catalogus), `log.md` (tijdlijn), `Het examen.md` (vorm en
praktisch), `Examensignalen.md` (wat de docent over het examen zei), `Oefenlog.md` (zwakke
plekken uit oefenexamens, ontstaat bij het eerste examen), `Oefenvragen.md` (vragen die de
moeite waard zijn om te bewaren).

## Navigatie

- **`index.md`**: elke pagina met één regel uitleg. Lees dit eerst bij een vraag, dan pas de
  pagina's zelf.
- **`log.md`**: alleen aanvullen. Formaat `## [JJJJ-MM-DD] <bouw|ingest|vraag|nakijken|examen> | titel`
  plus een of twee regels.

## Bewerkingen

### Ingest: er komt materiaal bij

1. Zet het in `00 Bronnen/` en draai `python3 _tools/extract.py "00 Bronnen"`. Kami-pdf met
   notities: ook `python3 _tools/notities.py <pdf>`.
2. Lees de bron. Bepaal welke topics, concepts, oefeningen en entities hij raakt.
3. Gaat het om een college: maak de `Lessen/`-notitie.
4. Werk elke geraakte pagina bij. Eén bron raakt vaak tien pagina's.
5. Zegt de bron iets over het examen: zet het in `Examensignalen.md`.
6. Spreekt de bron een bestaande pagina tegen: zet beide versies erin, zeg welke bron
   voorgaat volgens de regels hieronder, en meld het aan de student.
7. Nieuwe pagina's in `index.md`. Regel in `log.md`.

### Vraag: de student vraagt iets

1. Lees `index.md`, dan de pagina's die je nodig hebt. Pas daarna de ruwe bronnen, als het
   brein het antwoord niet heeft.
2. Antwoord met `[[wikilink]]`-verwijzingen naar wat je gebruikte.
3. Richt het antwoord op de examenvorm uit `Het examen.md`.
4. Was het antwoord nieuw werk (een vergelijking, een uitgewerkte casus, een verband):
   schrijf het als pagina, zet het in de index, log een `vraag`-regel.
5. Staat het nergens in de bronnen: zeg dat. Vul niet aan uit algemene kennis zonder te
   zeggen dat het niet uit de cursus komt.

### Nakijken: gaten en fouten zoeken

1. Draai `python3 _tools/nakijken.py .` voor dode links, weespagina's en de index.
2. Zoek daarna zelf naar:
   - tegenspraak tussen pagina's
   - verouderde stof (een nieuwere bron zegt iets anders)
   - begrippen die op drie of meer pagina's vallen zonder eigen pagina
   - examensignalen zonder uitgewerkte pagina
   - bronnen in `00 Bronnen/` zonder `ingest`-regel in de log
   - pagina's zonder bronvermelding
3. Lever een lijst op, gerangschikt op wat het meest telt voor het examen.
4. Mechanische fouten (index, links) herstel je meteen. Inhoudelijke fouten pas na akkoord
   van de student.
5. Regel `nakijken` in de log.

### Examen: de student wil zich testen

1. Lees `Het examen.md` voor de vorm, `Examensignalen.md` voor het gewicht, `Oefenlog.md`
   voor de zwakke plekken.
2. Vraag kort: welk deel of alles, hoeveel vragen (voorstel: tien), feedback per vraag of op
   het einde.
3. Maak de vragen in de echte examenvorm:
   - **Stellingen of meerkeuze.** Een casus of situatie plus opties, precies zoveel juiste als
     op het echte examen. Maak een optie fout met één woord (altijd, nooit, kan, enkel,
     slechts), een verwisseld begrip, een verkeerde termijn of drempel. Zo bouwt een docent
     ze ook.
   - **Open vraag.** De vraag, en voor jezelf de kernpunten die in een goed antwoord moeten
     staan. Scoor per kernpunt.
   - **Oefening.** Een variant van een pagina uit `Oefeningen/` met andere cijfers. Reken de
     oplossing eerst zelf volledig uit, controleer ze twee keer, en vraag de student om
     tussenresultaten.
   - **Mondeling.** Een vraag, dan doorvragen op het waarom tot het antwoord vastloopt of klopt.
4. Verdeling: volg het gewicht uit `Examensignalen.md`. Zijn er zwakke plekken in
   `Oefenlog.md`, haal daar een derde van de vragen uit.
5. Eén vraag tegelijk. Wacht op het antwoord. Geen hints tenzij de student erom vraagt.
6. Feedback: juist of fout, waarom, het woord of de stap waar het breekt, en de pagina waar
   het staat.
7. Op het einde: score, en in `Oefenlog.md` per fout de datum, het onderwerp, wat er misging
   en de pagina. Een vraag die goed werkte gaat naar `Oefenvragen.md`. Regel `examen` in de log.

Elke vraag komt uit het brein. Verzin geen feiten, artikelen of cijfers die er niet in staan.

## Welke bron gaat voor

Bij tegenspraak, van sterk naar zwak:

1. wat de docent in de les zei, gecontroleerd tegen de slides
2. de slides en de officiële cursus
3. officiële examenregels, modeloplossingen van de docent
4. de eigen notities van de student (sterk signaal van wat de docent benadrukte)
5. de eigen samenvatting van de student
6. samenvattingen en oplossingen van anderen (kunnen fouten bevatten, altijd nachecken)

## Harde regels

- **`00 Bronnen/` is onaanraakbaar.** Lezen, nooit bewerken.
- **Transcripties bevatten fouten.** Spraakherkenning maakt fouten in namen, vaktermen en
  getallen. Neem nooit een naam, getal, artikel of paginanummer uit een transcriptie over
  zonder het tegen de slides of een andere bron te leggen. Corrigeer stil bij het overnemen.
- **Oude opnames, nieuwe editie.** Verwijst een opname naar paginanummers, controleer ze
  tegen de huidige editie. Houd een mapping bij in `Paginas.md` als dat vaak gebeurt.
- **Altijd een bron.** Elke Concept- en Oefeningpagina noemt waar het vandaan komt.
- **Geen namen van medestudenten** uit klaslijsten of tekenlijsten.

## Regels voor dit vak

{{Wat tijdens de bouw bleek. Voorbeelden: "Boek 6 BW is nieuw sinds 2025, alles met art. 1382
oud BW is verouderd." "De transcriptie schrijft de naam van de prof als X, het is Y."
"Pagina's in de opnames zijn +4 ten opzichte van de 16e editie." Schrap dit blok als er
niets is.}}
