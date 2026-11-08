# Talk: Same standard, different readers

**Event:** Write the Docs
**Status:** Planned. Slides and speaker notes drafted; not yet delivered.
**Prepared for:** [Technical Editor, Editorial Publishing, Anthropic](https://job-boards.greenhouse.io/anthropic/jobs/5443997008)

## What this shows

Explaining model behavior to technical writers who don't work with AI models: what changes when a style guide becomes a prompt, why a passing automated check can hide a real problem, and how to read a small test honestly. Every number on the slides comes from logged runs in the [model variance kit](../../test-kit/model-variance-kit/), and each example names its model, run and the totals for its group.

## Abstract

Teams reuse a style guide across many writers. Now one of those writers is often an AI model, and the guide reaches it as a prompt. I gave five models the same house style standard and the same six passages, ran each five times, then took the standard away and ran them again. With the standard, the models agreed almost completely. Without it, an automated scanner still found nothing wrong, but a blind human editor found headings added and information reordered, while meaning held up about as well as with the standard. The talk covers what the standard bought, what the checks missed, and five habits for testing a standard that a model will read.

## Files

- [`slides.pptx`](slides.pptx): 18 slides with speaker notes on each.
- [`outline.md`](outline.md): the slide-by-slide outline with the source file for every number.
- [`build_talk_pptx.js`](build_talk_pptx.js): the script that generates the slides.

## Limitations

- The talk reports one small test: six passages, one review draft, five runs per model, one human scorer. It makes no claim beyond these models on these inputs, and does not rank models.
- One supported result may reflect drift in my own scoring; the talk says so on slide 15.
