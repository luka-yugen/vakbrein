---
name: vakbrein examenstof
description: One-time exam briefing for a course brain, built as a Leitner box of ruled index cards.
colors:
  box: "#1d4ed8"
  box-deep: "#1740b4"
  box-ink: "#e3ebff"
  box-dim: "#b7c9f7"
  card: "#ffffff"
  ink: "#15171c"
  ink-2: "#4a5061"
  rule: "#c7d8f6"
  red: "#e5383b"
  mark: "rgba(255,221,64,.9)"
  postit: "#ffe98a"
  postit-ink: "#3b3208"
  ok: "#12805c"
  no: "#c62f32"
  tab-yellow: "#ffd966"
  tab-green: "#9fe0b4"
  tab-pink: "#ffb3cf"
  tab-blue: "#a9d4ff"
  tab-orange: "#ffc58f"
  tab-lilac: "#d7c4ff"
  tab-grey: "#f2f2ea"
typography:
  display:
    fontFamily: "Bricolage, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(44px, 9vw, 92px)"
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: "-0.04em"
    fontVariation: "'wdth' 88"
  headline:
    fontFamily: "Bricolage, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(22px, 3.2vw, 28px)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  verdict:
    fontFamily: "Bricolage, ui-sans-serif, system-ui, sans-serif"
    fontSize: "26px"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Bricolage, ui-sans-serif, system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 700
    lineHeight: "28px"
  title-sm:
    fontFamily: "Bricolage, ui-sans-serif, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 700
    lineHeight: "28px"
  body:
    fontFamily: "ui-sans-serif, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "28px"
  label:
    fontFamily: "Bricolage, ui-sans-serif, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    lineHeight: 1
  small:
    fontFamily: "ui-sans-serif, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: "18px"
  command:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "16px"
    fontWeight: 500
    lineHeight: "28px"
  path:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: "28px"
rounded:
  mark: "2px"
  card: "6px"
  control: "8px"
  tab: "9px 9px 0 0"
  postit: "2px 2px 14px 2px"
  step: "50%"
spacing:
  line: "28px"
  page-gutter: "16px"
  card-gutter: "28px"
  card-gutter-mobile: "18px"
  card-gap: "28px"
  grid-gap: "22px"
  page-end: "96px"
components:
  index-card:
    backgroundColor: "{colors.card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "0 28px 28px"
  divider-tab:
    backgroundColor: "{colors.tab-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.tab}"
    padding: "11px 14px 16px"
  postit:
    backgroundColor: "{colors.postit}"
    textColor: "{colors.postit-ink}"
    typography: "{typography.command}"
    rounded: "{rounded.postit}"
    padding: "14px 50px 14px 16px"
  copy-button:
    textColor: "{colors.postit-ink}"
    rounded: "{rounded.control}"
    width: "32px"
    height: "28px"
  copy-button-done:
    textColor: "{colors.ok}"
  answer-option:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "7px 10px"
  flip-button:
    textColor: "{colors.box}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "10px 12px"
  step-marker:
    textColor: "{colors.red}"
    rounded: "{rounded.step}"
    size: "36px"
---

# Design System: vakbrein examenstof

## Overview

**Creative North Star: "The Leitner Box"**

The page is a cobalt card box seen from above. Each section is a white ruled index card with a red header rule, filed behind colored cardboard divider tabs. Everything the student reads sits on a 28px ruled line, the way handwriting sits on a system card. Exam weight is drawn with a yellow highlighter, commands for the AI are stuck on as post-it notes, and practice questions are real cards you flip.

Density is calm and single-column: one card per topic, read once from front to back. The front card is the only loud moment, with the course name in huge Bricolage Grotesque. After that the system holds back and lets the ruled lines, the highlighter and the post-its carry the voice. The world was chosen over a tile dashboard and over a cream notebook page.

**Key Characteristics:**
- Cobalt box as the ground, white cards as the only reading surface.
- A 28px line grid that text, lists, forms and gaps all respect.
- Stationery props (tabs, highlighter, post-its, flip cards) each with one job.
- One embedded display face, system sans for reading, system mono for commands.
- Works offline, in light and dark, in print, and with reduced motion.

## Colors

A saturated cobalt ground with paper-white cards, and a small set of stationery colors that each mean one thing.

### Primary
- **Cobalt Box** (box, with Box Deep as the lower end of the body gradient): the page ground behind all cards, also the ink of interactive text on cards (option letters, flip buttons, option hover border).
- **Box Ink** and **Box Dim**: text that sits directly on the cobalt, only the footer. Box Ink is the footer line and its link (5.6:1 on the cobalt); Box Dim is kept as a token but not used for text.

### Secondary
- **Header Red** (red): the 2px rule under every card and flip-card header, and the numbered step circles. It is the red line of a system card, nothing else.
- **Highlighter Yellow** (mark): the marker stroke. Used for exam weight bars, marked signal words, the countdown and the exam tip.
- **Post-it Yellow** (postit) with **Post-it Ink**: the note surface for things to say to the AI. Post-it Yellow is also the focus ring color on the cobalt.

### Tertiary
- **Divider Tabs** (tab-yellow, tab-green, tab-pink, tab-blue, tab-orange, tab-lilac, tab-grey): one pastel per navigation tab, in fixed order by position. Tab text is always near-black (#1c1f27) because every tab is light.
- **Right Green** (ok) and **Wrong Red** (no): the verdict on a flipped practice card, and the green check on a copied post-it.

### Neutral
- **Card White** (card): the index card and flip-card surface.
- **Card Ink** (ink): body text on cards.
- **Pencil Grey** (ink-2): secondary text on cards: header notes, reasons, paths, form labels, the score line, hints.
- **Ruling Blue** (rule): the ruled lines on cards, flip-card borders and option borders.

Dark mode (prefers-color-scheme) deepens the box to #0d1a4a / #0a143a, dims its text to #dfe7ff / #9fb2e6, and turns cards into a grey-white card (#e9ecf2, ink #14161b, ink-2 #454b5b, rule #b3c3e2). The post-it softens to #e9d67a and the card shadow darkens. Cards stay light in dark mode: they are paper.

### Named Rules
**The One Job Rule.** Each stationery color means one thing. Highlighter means weight or emphasis, post-it means "say this to your AI", red belongs to the card's header line and its step numbers. Never use a post-it for a note that is not a command, or a highlight for decoration.

**The Paper Stays Paper Rule.** Cards never go dark. In dark mode only the box darkens; the card becomes an off-white card with the same ink.

## Typography

**Display Font:** Bricolage Grotesque, embedded as a woff2 data URI under the family name "Bricolage" (weights 200 to 800, stretch 75% to 100%, font-display swap), falling back to ui-sans-serif and system-ui.
**Body Font:** the system sans (ui-sans-serif, -apple-system, Segoe UI, Roboto).
**Mono Font:** the system mono (ui-monospace, SFMono-Regular, Menlo) for commands and source paths.

**Character:** a loud, slightly condensed grotesque for card titles and labels against a quiet system sans for reading. The mono marks anything the student types or can look up.

### Hierarchy
- **Display** (800, clamp 44px to 92px, line-height 0.95, stretch 88%): the course name on the front card only.
- **Headline** (700, clamp 22px to 28px, 1.1): card titles.
- **Verdict** (800, 26px, 1.1): "Juist" or "Niet juist" on a flipped card, in green or red.
- **Title** (700, 18px on the 28px line): step titles, the countdown line.
- **Title Small** (700, 16px to 17px on the 28px line): exam form labels, question text, weight block names.
- **Body** (400, 16px, 28px line): all running text. Column width follows the card (max 868px), post-its cap at 620px.
- **Label** (600, 13px): divider tabs, flip buttons, flip-card headers.
- **Small** (13px, 18px line): card header notes and meta line, in Pencil Grey.
- **Command** (mono 500, 16px, 28px line): the text on a post-it, wraps anywhere.
- **Path** (mono, 13px): brain page paths and sources, in Pencil Grey.

### Named Rules
**The Line Height Is The Grid Rule.** Every text role that lives on a card uses a 28px line-height, so text sits on the ruled lines. Only display, headline, verdict and small labels step off the grid.

**The One Face Rule.** Bricolage is the only webfont and it is embedded. Nothing is fetched from outside the file.

## Layout

A single centered column of cards (max 900px, 16px side gutter, 96px bottom padding) on the cobalt box. Cards are 28px apart; the front card sits 22px from the tabs. Inside a card the header has 28px side padding and the ruled body starts one line (28px) below it.

The 28px line (var --lh) is the spacing unit on cards: paragraph gaps, list gaps, form rows, grid row gaps and card bottom padding are all one line. Horizontal gaps between grid items are 22px. The exam facts are a two-column form (label column 120px to 190px, 20px gap). AI commands lay out in an auto-fill grid of 250px minimum; practice cards in an auto-fill grid of 300px minimum.

At 640px and below, card gutters shrink to 18px, the exam form stacks to one column with a line of space between rows, and step indents shrink from 52px to 46px. The tab strip scrolls horizontally with a fade mask on the right edge and hidden scrollbar. Anchor jumps leave 76px of scroll padding for the sticky tabs.

Print drops the box color, hides tabs, copy buttons and flip buttons, swaps card shadows for a 1px grey border, avoids breaking inside a card, shows both sides of every flip card flat, and draws the highlighter bars at full length.

## Elevation & Depth

Depth is physical: the cards stand in a box. Cards carry a two-part shadow (a 1px contact line plus a soft 24px drop) tinted toward navy. The front card shows two faded card edges behind it (55% and 30% opacity) so the stack reads as a box of cards. Post-its have their own warmer, shorter shadow and a slight rotation. Flip cards sit lower than index cards, with a 1px ruled border and a small shadow. Tabs have an inset bottom shade so they look tucked behind the front card.

### Shadow Vocabulary
- **Card in the box** (`0 1px 1px rgba(8,20,70,.18), 0 10px 24px -8px rgba(8,20,70,.45)`; dark: `0 1px 1px rgba(0,0,0,.4), 0 12px 28px -8px rgba(0,0,0,.7)`): every index card.
- **Post-it** (`0 1px 1px rgba(0,0,0,.12), 0 8px 14px -8px rgba(60,45,0,.55)`): post-it notes.
- **Practice card** (`0 1px 0 var(--rule), 0 6px 16px -10px rgba(8,20,70,.5)`): flip-card faces.
- **Tucked tab** (`inset 0 -6px 8px -6px rgba(0,0,0,.25)`): divider tabs.

### Named Rules
**The Physical Object Rule.** A shadow means the thing is a separate piece of paper. Controls on a card (options, buttons) get borders, not shadows.

## Shapes

Paper corners. Cards and flip cards have a small 6px radius. Divider tabs are rounded on top only (9px). Post-its are square except for a curled bottom-right corner (14px) and sit rotated between -0.5deg and 0.5deg. Controls use an 8px radius, the copy button 7px. The highlighter stroke is a hand-drawn polygon (clip-path) with uneven corners and a -0.4deg tilt; inline marks are a soft band covering 76% to 80% of the line height. Step numbers are 36px circles with a 2px red outline. Icons are inline 20px-viewBox SVG strokes at 16px (copy, check, flip).

## Components

### Index Card
The system card; every section is one.
- **Corner Style:** 6px.
- **Background:** Card White with Ruling Blue lines every 28px in the body, drawn as a repeating gradient.
- **Header:** title left, a small grey note right (source page or a count), 2px Header Red rule underneath, wraps on narrow screens.
- **Shadow Strategy:** Card in the box.
- **Front card:** a taller header with the Display course name, a meta line (code · lecturer · program), the countdown with the day count highlighted, the intro sentence, and the first post-it. Two faded card edges peek out above it.
- **Empty data hides the card:** an empty list removes its card and its tab.

### Divider Tabs (navigation)
- **Style:** sticky strip at the top with a cobalt fade behind it; each tab is a Label-type pastel card tab in fixed color order.
- **States:** at rest a tab sits 6px lower; hover and the current section raise it to 0 (0.25s, cubic-bezier(.2,.8,.2,1)). The current tab follows scrolling via aria-current.
- **Mobile:** scrolls sideways with a right-edge fade.

### Post-it (command note)
The thing to say to your AI.
- **Style:** Post-it Yellow, Command mono text, optional 13px Bricolage label above ("zeg dit tegen je AI"), curled corner, slight rotation, max 620px wide (full width inside the AI grid, each with its own tilt).
- **Copy button:** 32 by 28px, top right, translucent white with a thin ink border, 7px radius. Hover makes it more opaque. On click it copies (clipboard API with a textarea fallback), swaps to a green check for 1.8s, then returns. Its accessible name includes the full command.

### Highlighter Bar (weight)
- **Style:** a yellow hand-drawn stroke behind the block name, length = weight x 20% (minimum 18%). A hidden text says "gewicht N van 5".
- **Motion:** if the card starts below the fold, bars draw in from the left when 30% of the card is visible, 0.9s cubic-bezier(.16,1,.3,1), staggered 90ms per row. No animation for cards already on screen, in print, or with reduced motion.

### Practice Flip Card
- **Style:** a small ruled card with a header row (tag left, "n/total · voorkant/achterkant" right) and a red rule.
- **Multiple choice:** options are full-width buttons with a letter in cobalt Bricolage, translucent white fill, 1.5px Ruling Blue border, 8px radius. Hover turns the border cobalt; focus shows a 3px cobalt outline.
- **Flip:** choosing an answer turns the card 180deg on Y (0.7s, cubic-bezier(.16,1,.3,1)) to show the Verdict in green or red and the explanation. Only the first answer counts toward the score. Focus moves to the back's button; aria-hidden swaps between sides.
- **Open question:** shows an italic grey hint to answer out loud and a "draai om" button; the back shows the answer.
- **Flip button:** cobalt Label text with a flip icon, no fill, faint cobalt wash on hover.
- **Score:** a polite live line under the grid: "x van y juist" plus the command for more practice.

### Numbered Steps
- **Style:** red outlined circle with a Bricolage number, Title-type step name, body text, and an optional post-it. One line between steps.

### Exam Form
- **Style:** a two-column definition list on the ruled lines, labels in Title Small Pencil Grey, values in Body. Followed by the tip as a highlighted sentence.

### Focus
Every focusable element shows a 3px Post-it Yellow outline with 2px offset and 4px radius; answer options use a cobalt outline instead because they sit on white.

## Do's and Don'ts

### Do:
- **Do** put every line of card text on the 28px grid (line-height 28px, gaps in multiples of 28px).
- **Do** make every command a post-it with a copy button, and nothing else a post-it.
- **Do** encode weight with the highlighter bar length (weight x 20%), with the number in hidden text.
- **Do** name the source brain page in the card header note or as a mono path.
- **Do** keep cards light in dark mode and let only the box darken.
- **Do** give every motion a reduced-motion and print fallback: the final state, drawn flat.

### Don't:
- **Don't** add tiles, metric boxes or a dashboard grid; the page is a stack of cards.
- **Don't** fetch fonts, scripts or images from outside the file; the page must work offline.
- **Don't** use the highlighter or Header Red as decoration.
- **Don't** put shadows on controls inside a card; only separate pieces of paper cast shadows.
- **Don't** add a second webfont or use Bricolage for running text.
