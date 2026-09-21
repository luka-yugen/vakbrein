# De studielaag: examenstof.html

Eén HTML-bestand in de hoofdmap van het brein. De student opent het in een browser, op laptop
of gsm, ook zonder internet. Het is de laag om mee te studeren. Het brein is de laag om in
op te zoeken.

## Werkwijze

1. Kopieer `<skill>/assets/examenstof.html` naar `examenstof.html` in de hoofdmap.
   Bestaat er al een: werk die bij, begin niet opnieuw. Zo blijven de vinkjes van de student.
2. Vul elk blok met `<!-- VUL: ... -->`. Haal de commentaarregel daarna weg.
3. Vul `PLAN` en `VRAGEN` in het script onderaan.
4. Open het bestand in een browser als je dat kan, en kijk het na op gsm-breedte (375 px)
   en in licht en donker.
5. Regel in `Brain/log.md`: `## [datum] studielaag | examenstof.html bijgewerkt`.

## Waar de inhoud vandaan komt

Alles komt uit het brein. Niets nieuws verzinnen. Staat iets niet in het brein, dan staat
het ook niet in de studielaag.

| sectie | bron |
|---|---|
| Wat je op het examen krijgt | `Brain/Het examen.md` |
| Hoe de docent vragen stelt | de sterkste vijf of zes uitspraken uit `Brain/Examensignalen.md`, met citaat |
| Studieplan | de Topics, gerangschikt op gewicht uit Examensignalen, verdeeld over de dagen tot het examen |
| Per blok | per Topic: wat je moet kunnen, de valkuilen, de breinpagina's |
| Oefenvragen | `Oefenvragen.md`, `Voorbeeldexamen.md`, oude examens. Aangevuld tot 10 à 20 vragen |
| Nog na te kijken | "Openstaande punten" in `AGENTS.md` |

## Het studieplan

- Van zwaar naar licht. Wat de docent het meest benadrukte en wat het meeste punten geeft
  eerst.
- Tel de dagen tot de examendatum. Verdeel de blokken over die dagen, met de laatste dag
  voor herhaling en oefenvragen. Geen datum bekend: laat `dag` weg.
- Elk blok is iets wat je in één zit doet: een titel, wat je concreet doet, een ruwe duur,
  en het pad naar de breinpagina.
- Een `id` verandert nooit meer als het er staat. Anders verliest de student zijn vinkjes.

## De oefenvragen

- Zelfde vorm als het echte examen. Meerkeuze op het examen: `type:"mc"`. Open vragen of
  oefeningen: `type:"open"` met de kernpunten of de uitkomst als antwoord.
- De uitleg bij een meerkeuzevraag zegt waarom het juiste antwoord klopt en welk woord of
  welke stap de andere fout maakt.
- Aanhalingstekens in teksten escapen, het is JavaScript.

## Ontwerp

Het sjabloon is af. Verander de opmaak niet, vul alleen in. Wat het al doet en zo moet blijven:

- één kolom van max 860 px, 16 px marge aan de zijkant, leesbaar op een gsm
- licht en donker volgens het systeem, met een knop om te wisselen
- een balk bovenaan met voortgang en score, die meescrollt
- vinkjes en antwoorden in de browser bewaard, per vak een eigen sleutel (de `<title>`)
- printbaar: bij afdrukken verdwijnen de knoppen en staan alle antwoorden open
- geen externe bestanden of lettertypes, zodat het offline werkt

Opmaak binnen de tekst: `<b>` voor wat van buiten moet of het zwaarst weegt, `<code>` voor
paden en artikelnummers, een `card warn` voor een studietip, een `card bad` voor een
bekende valkuil. Spaarzaam: staat alles in het vet, valt niets meer op.

Verander de `<title>` niet meer nadat de student begonnen is, dat is de opslagsleutel.
