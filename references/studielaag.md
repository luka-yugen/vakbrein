# De studielaag: examenstof.html

Eén HTML-bestand in de hoofdmap van het brein. Het is een briefing: de student leest hem één
keer, aan het begin, en weet dan wat er op het examen komt, wat het zwaarst weegt, hoe de
docent vragen stelt, hoe te beginnen, en wat te zeggen tegen de AI. Het leren zelf gebeurt
daarna in de chat met het brein. Werkt offline, op laptop en gsm, in licht en donker, en
is printbaar.

## Werkwijze

1. Kopieer `<skill>/assets/examenstof.html` naar `examenstof.html` in de hoofdmap.
   Bestaat hij al: werk alleen het `VAK`-object bij.
2. Vul het `VAK`-object in het script onderaan. Verder niets aanpassen: de opmaak, het
   ingebakken lettertype en de code blijven zoals ze zijn.
3. Open het bestand in een browser als je dat kan, en kijk het na op gsm-breedte.
4. Regel in `Brain/log.md`: `## [datum] studielaag | examenstof.html bijgewerkt`.

## Het VAK-object

Alles komt uit het brein. Niets verzinnen. Een lege lijst (`[]`) laat die kaart weg.

| veld | inhoud | bron |
|---|---|---|
| `naam`, `code`, `docent`, `opleiding` | kop van de voorste kaart | `AGENTS.md` |
| `bronnen`, `bijgewerkt` | voetregel | inventaris, datum van vandaag |
| `examen.datum` | ISO-datum en uur, voor de aftelling; leeg als onbekend | `Het examen.md` |
| `examen.tekst` | de datum zoals je hem zegt: "vrijdag 15 januari, 9u00" | idem |
| `examen.rijen` | `[label, tekst]` per feit: vorm, vraagtype, hulpmiddelen, cijfer | idem |
| `examen.tip` | wat die vorm betekent voor hoe je studeert, twee zinnen | idem |
| `begin.zin` | wat deze pagina is, twee zinnen | vast, pas de taal aan |
| `begin.zeg` | de eerste zin die de student tegen de AI zegt | het zwaarste blok |
| `gewicht` | per Topic: `blok`, `gewicht` 1 tot 5, `waarom`, `pagina` | `Examensignalen.md`, `Het examen.md` |
| `signalen` | drie tot vijf uitspraken van de docent over hoe vragen gebouwd worden, `woorden` die gemarkeerd worden, `bron` (de les) | `Examensignalen.md` |
| `stappen` | drie tot vijf stappen om te beginnen, elk met `titel`, `uitleg` en `zeg` | afgeleid uit het gewicht |
| `ai` | vier opdrachten voor de AI met wat ze doen | vaste lijst, pas voorbeelden aan het vak aan |
| `vragen` | drie tot zes proefvragen in de echte examenvorm | `Oefenvragen.md`, `Voorbeeldexamen.md`, oude examens |
| `open` | wat nog nagekeken moet worden | "Openstaande punten" in `AGENTS.md` |

Opmaak in teksten: `**zo**` wordt vet. Gebruik het voor wat van buiten moet of het zwaarst
weegt, spaarzaam. Aanhalingstekens escapen, het is JavaScript.

## De inhoud

- **Gewicht** is een oordeel, geen gevoel. 5 is wat de docent het meest benadrukte of wat de
  meeste punten geeft. De lengte van de markeerstreep volgt het gewicht.
- **Stappen** eindigen altijd in iets wat de student tegen de AI zegt. Begin bij het zwaarste
  blok, laat testen voor herhalen komen.
- **Vragen** in de vorm van het echte examen: meerkeuze als `type:"mc"` met `opties`, `juist`
  (index vanaf 0) en een `uitleg` die zegt welk woord of welke stap de andere opties fout
  maakt. Open vragen of oefeningen als `type:"open"` met de kernpunten of de uitkomst.
  Het zijn proefkaarten: het echte oefenen gebeurt met `/vakbrein examen`.

## Ontwerp

Het sjabloon is af: een kobaltblauwe kaartenbak met gelijnde systeemkaarten, gekleurde
tabbladen als navigatie, markeerstiften voor gewicht, post-its met kopieerknop voor wat je
tegen je AI zegt, en proefkaarten die je omdraait. De tekst staat op een raster van 28 px
dat samenvalt met de lijnen van de kaarten. Verander de opmaak niet. Wil je een vak een
eigen kleur geven, pas dan alleen `--box` en `--box-deep` aan.
