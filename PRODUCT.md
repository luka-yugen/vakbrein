# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS with a little vanilla JS, one self-contained file per brain (`examenstof.html`), no external requests so it works offline. Template lives at `assets/examenstof.html`; a demo is published from `docs/` on GitHub Pages.

## Users

University students (first user: a Handelswetenschappen student at UGent, Flemish Dutch) who have built a study brain for one course with the vakbrein skill. They open the study page once, at the start of studying a course, to understand the exam and how to begin. The actual studying happens afterwards in a chat with an agentic AI (Claude Code or another tool) that reads the brain.

## Product Purpose

vakbrein turns all material for one course into a linked markdown wiki (the brain) that an AI maintains and uses to answer questions, run practice exams and track weak spots. The study page is the one-time briefing on top of that brain: what the exam looks like, what weighs most, how the lecturer builds questions, a plan for how to start, and the exact things to say to the AI to learn and practice. Success: after one read the student knows what to do first and starts a session with the AI.

## Positioning

Other study tools are the place where you study. This page is a briefing that sends you to the place where you study: an AI that knows your course material, including what the lecturer said about the exam.

## Operating Context

Read once on a laptop, sometimes on a phone. The student then works in a terminal or chat with commands like `/vakbrein examen`, or plain sentences in tools without the skill. Material comes from slides, lecture transcripts, own summaries, Kami-annotated PDFs, exercises and old exams.

## Capabilities and Constraints

Content comes only from the brain (`Brain/Het examen.md`, `Examensignalen.md`, Topics, `Oefenvragen.md`, `AGENTS.md`). Nothing invented. Filled in by an AI from a template, so structure must be easy to fill: data arrays plus clearly marked blocks. Must work offline, on mobile, in light and dark, and print. Language of the page follows the course material (Dutch by default).

## Brand Commitments

The skill is public and shareable (github.com/luka-yugen/vakbrein), MIT. Writing style: plain Dutch, short sentences, no em dashes, no filler.

## Evidence on Hand

Demo content is fictional (a made-up Statistiek I course) and labelled as such. No real student numbers, testimonials or results exist; none may be invented.

## Product Principles

- The page sends you to the AI. Every section ends in something to do or say.
- Exam first: the real exam format decides what matters on the page.
- Truth from the brain only, with the source page named.
- Readable in one sitting, then done.
