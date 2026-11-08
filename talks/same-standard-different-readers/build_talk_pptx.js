// Builds the talk deck as a structured .pptx from the published Slides deck's content.
// Canvas: LAYOUT_WIDE (13.333 x 7.5 in). Source deck is 1920 x 1080 px: 1 px = 1/144 in, 2 px = 1 pt.
// Usage: SKILL=<pptx skill dir, for scripts/apply_theme.js> NODE_PATH=<dir with pptxgenjs@3.12.0> node build_talk_pptx.js slides.pptx
const pptxgen = require("pptxgenjs");
const { applyTheme } = require(process.env.SKILL + "/scripts/apply_theme.js");
const OUT = process.argv[2];

const THEME = {
  name: "Same Standard",
  headFontFace: "Arial",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "16202C", lt1: "F4F6F8", dk2: "3C4858", lt2: "FBFCFD",
    accent1: "2559B8", accent2: "C7621A", accent3: "7FA8F0", accent4: "F2A25C",
    accent5: "5B6676", accent6: "D5DBE3", hlink: "2559B8", folHlink: "5B6676",
  },
};
const MONO = "Courier New";
const X = 0.889, W = 11.556; // 128 px margins, 1664 px content width
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title = "Same Standard, Different Readers";
pres.author = "Kathryn Collins";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;

const eyebrowPh = (color) => ({ placeholder: { options: { name: "eyebrow", type: "body", x: X, y: 0.889, w: W, h: 0.32, fontSize: 12, bold: true, charSpacing: 2, color, margin: 0, valign: "top" }, text: "" } });
const titlePh = (y, color) => ({ placeholder: { options: { name: "title", type: "title", x: X, y, w: W, h: 1.25, fontFace: THEME.headFontFace, fontSize: 36, bold: true, color, margin: 0, valign: "top", align: "left" }, text: "" } });
const footerPh = (color) => ({ placeholder: { options: { name: "footer", type: "body", x: X, y: 6.86, w: W, h: 0.3, fontSize: 12, color, margin: 0, valign: "top" }, text: "" } });

pres.defineSlideMaster({ title: "Light, eyebrow and title", background: { color: C.background1 }, objects: [eyebrowPh(C.accent1), titlePh(1.3, C.text1), footerPh(C.accent5)] });
pres.defineSlideMaster({ title: "Light, title only", background: { color: C.background1 }, objects: [titlePh(0.889, C.text1), footerPh(C.accent5)] });
pres.defineSlideMaster({ title: "Dark, eyebrow and title", background: { color: C.text1 }, objects: [eyebrowPh(C.accent3), titlePh(1.3, C.background1), footerPh("9AA6B6")] });
pres.defineSlideMaster({ title: "Dark statement", background: { color: C.text1 }, objects: [footerPh("9AA6B6")] });
pres.defineSlideMaster({ title: "Accent statement", background: { color: C.accent1 }, objects: [footerPh("D6E2F8")] });

const T = (slide, text, o) => slide.addText(text, Object.assign({ isTextBox: true, margin: 0, valign: "top", fontFace: THEME.bodyFontFace, color: C.text2 }, o));
const card = (slide, x, y, w, h, name, extra) => slide.addShape(pres.shapes.ROUNDED_RECTANGLE, Object.assign({ x, y, w, h, rectRadius: 0.11, fill: { color: C.background2 }, line: { color: C.accent6, width: 0.75 }, objectName: name }, extra || {}));
const rule = (slide, x, y, w, color, name) => slide.addShape(pres.shapes.LINE, { x, y, w, h: 0, line: { color, width: 2.25 }, objectName: name });
const eyebrowLabel = (slide, text, x, y, w, color, name) => T(slide, text.toUpperCase(), { x, y, w, h: 0.3, fontSize: 12, bold: true, charSpacing: 1.5, color, objectName: name });
let section = "";
const add = (masterName, sec) => { if (sec !== section) { pres.addSection({ title: sec }); section = sec; } return pres.addSlide({ masterName, sectionTitle: sec }); };
const S1 = "The question and how the test worked", S2 = "With the standard, the models agreed", S3 = "Taking the standard away", S4 = "What our instruments missed", S5 = "Results and what to take back";

// 1 cover
let s = add("Dark statement", S1);
T(s, "CONTENT REUSE WHEN THE READER IS A MODEL", { x: X, y: 1.75, w: W, h: 0.32, fontSize: 12, bold: true, charSpacing: 2, color: C.accent3, objectName: "Eyebrow" });
T(s, "Same standard, different readers", { x: X, y: 2.25, w: W, h: 1.9, fontFace: THEME.headFontFace, fontSize: 60, bold: true, color: C.background1, objectName: "Title" });
T(s, "What five models did with one style guide", { x: X, y: 4.35, w: W, h: 0.5, fontSize: 22, color: "BCC6D3", objectName: "Subtitle" });
s.addText("Write the Docs · Kathryn Collins", { placeholder: "footer" });
s.addNotes("Welcome. This talk is about one experiment: we gave five language models the same house style standard and the same six passages, ran each one five times, and scored what came back, automatically and blind by a human editor. Then we took the standard away and did it again. Everything here comes from pre-registered runs; the kit and raw logs are available at the end.");

// 2 the question
s = add("Light, eyebrow and title", S1);
s.addText("THE QUESTION", { placeholder: "eyebrow" });
s.addText("The writer is often a model now, and the style standard is its prompt", { placeholder: "title" });
T(s, [
  { text: "Give five models the same standard and the same passages.", options: { breakLine: true, paraSpaceAfter: 8 } },
  { text: "How much do they differ from each other, and from run to run?", options: { breakLine: true, paraSpaceAfter: 8 } },
  { text: "What does the standard buy compared with no standard at all?" },
], { x: X, y: 2.75, w: W, h: 1.6, fontSize: 16, objectName: "Questions" });
["Haiku 5.5", "Sonnet 5.5", "Opus 5.5", "Fable 5.1", "Opus 4.7"].forEach((m, i) => {
  s.addText(m, { x: X + i * 1.85, y: 5.75, w: 1.7, h: 0.5, shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.25, fill: { color: "E3E9F2" }, fontFace: THEME.bodyFontFace, fontSize: 14, color: C.text1, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: "Model " + m });
});
s.addNotes("We reuse style standards across writers all the time. More and more, one of those writers is a model, and the standard reaches it as a prompt. So the question was simple: hand five models one standard and the same passages. How different are they from each other, and from themselves run to run? And what does the standard actually buy you compared with giving them nothing? No ranking of models in this talk: the design only supports “these models behaved like this on these inputs.”");

// 3 method
s = add("Light, title only", S1);
s.addText("How the test worked", { placeholder: "title" });
const cards = [
  ["Pre-registered", "Hypotheses, metrics and honesty rules fixed before any call. No re-runs, no exclusions."],
  ["Six trap passages", "Each built around a rule that can cost substance: a caveat after a dash, a permission “you”, a product name that is also a buzzword."],
  ["One review task", "A draft with 12 planted violations and 4 correct-but-suspicious distractors."],
  ["Three kinds of scoring", "The house scanner, substance checks, and blind human scoring of meaning and naturalness."],
];
cards.forEach(([h, b], i) => {
  const cx = X + (i % 2) * 5.861, cy = 2.05 + Math.floor(i / 2) * 2.12, cw = 5.694, ch = 1.95;
  card(s, cx, cy, cw, ch, "Card " + h);
  T(s, h, { x: cx + 0.25, y: cy + 0.25, w: cw - 0.5, h: 0.45, fontFace: THEME.headFontFace, fontSize: 22, bold: true, color: C.accent1, objectName: "Card title " + h });
  T(s, b, { x: cx + 0.25, y: cy + 0.8, w: cw - 0.5, h: 1.0, fontSize: 14, color: C.text2, objectName: "Card text " + h });
});
s.addText("5 runs per model per input · 456 calls, none failed", { placeholder: "footer" });
s.addNotes("Everything was written down before the first call: the hypotheses, the metrics, and rules like no re-running to get a better result and no exclusions. The six passages are traps: each one has a rule that, followed too literally, drops something a reader needs. The other passages are a legitimate “just”, a procedure, and a code block with a review flag. The review task asks the model to list violations in a draft where we planted 12 and added 4 pieces of correct text that look suspicious. Five runs per model per input, 456 calls in total, none failed. One call was aborted and kept but not scored.");

// stat row helper
const stats = (slide, items, y, numSize) => {
  const n = items.length, gap = 0.167, w = (W - gap * (n - 1)) / n;
  items.forEach(([num, label, color], i) => {
    const x = X + i * (w + gap);
    rule(slide, x, y, w, color || C.accent1, "Rule " + label);
    T(slide, num, { x, y: y + 0.17, w, h: numSize / 72 * 1.15, fontFace: THEME.headFontFace, fontSize: numSize, bold: true, color: C.text1, objectName: "Stat " + label });
    T(slide, label, { x, y: y + 0.22 + numSize / 72 * 1.15, w, h: 0.6, fontSize: 14, color: C.text2, objectName: "Label " + label });
  });
};

// 4 agreed
s = add("Light, eyebrow and title", S2);
s.addText("WITH THE STANDARD", { placeholder: "eyebrow" });
s.addText("The five models agreed", { placeholder: "title" });
stats(s, [["0", "scanner blockers"], ["0", "substance checks lost"], ["12/12", "planted violations found"], ["0", "distractors flagged"]], 2.45, 60);
T(s, [{ text: "One rule did not hold: rule 7 says “just” is often legitimate. Guided rewrites removed the meaningful “just” in " }, { text: "38 of 40", options: { bold: true } }, { text: " runs." }], { x: X, y: 4.75, w: W, h: 0.8, fontSize: 16, objectName: "Just note" });
s.addText("Every model, every input, main and added-models runs", { placeholder: "footer" });
s.addNotes("With the standard in the prompt, the models agreed. Zero scanner blockers, zero substance checks lost, on every input, for every model. In the review task, 12 of 12 planted violations and zero distractors, every run in the main and added-models sets. The replication had one small exception I’ll come back to. One rule did not hold: rule 7 tells the writer that “just” is often legitimate. Input 04 has a “just” that carries meaning, and the guided rewrites removed it in 38 of 40 runs across all three guided sets.");

// quote box helper
const quote = (slide, label, labelColor, text, y, h, opts) => {
  const o = Object.assign({ x: X, w: W, size: 15, textColor: C.text1 }, opts || {});
  card(slide, o.x, y, o.w, h, "Box " + label);
  eyebrowLabel(slide, label, o.x + 0.25, y + 0.22, o.w - 0.5, labelColor, "Label " + label);
  T(slide, text, { x: o.x + 0.25, y: y + 0.6, w: o.w - 0.5, h: h - 0.8, fontFace: MONO, fontSize: o.size, color: o.textColor, objectName: "Text " + label, lineSpacingMultiple: o.lsm || 1.15 });
};

// 5 example A
s = add("Light, eyebrow and title", S2);
s.addText("EXAMPLE A · MODELS AGREEING", { placeholder: "eyebrow" });
s.addText("The caveat stays, the code stays", { placeholder: "title" });
quote(s, "Original, input 06", C.accent5, "It’s important to note that the alert can take up to 30 seconds to appear — this is expected.", 2.45, 1.45, { textColor: C.text2 });
quote(s, "Rewrite · Sonnet 5.5, main run, run 1", C.accent1, "The alert can take up to 30 seconds to appear; this is expected.", 4.05, 1.05);
T(s, [{ text: "Code block and " }, { text: "[VERIFY: …]", options: { color: C.accent1 } }, { text: " flag unchanged. All 10 sampled guided rewrites of input 06 were scored meaning preserved." }], { x: X, y: 5.3, w: W, h: 0.75, fontSize: 14, objectName: "Example A note" });
s.addText("Cell: Sonnet 5.5, input 06, 5 runs · 0 blockers · 0 substance lost", { placeholder: "footer" });
s.addNotes("Here’s what agreement looks like. Input 06 has a stock AI phrase, a dash, a code block and a review flag. Sonnet’s first run drops the phrase, swaps the dash for a semicolon, and leaves the code and the VERIFY flag exactly alone. All five models handled this input the same way, and in the human sample all 10 guided rewrites of it kept the meaning.");

// two-card helper
const twoCards = (slide, items, y, h) => items.forEach(([head, body], i) => {
  const cw = 5.694, cx = X + i * 5.861;
  card(slide, cx, y, cw, h, "Card " + head);
  T(slide, head, { x: cx + 0.25, y: y + 0.25, w: cw - 0.5, h: 0.45, fontFace: THEME.headFontFace, fontSize: 22, bold: true, color: C.text1, objectName: "Card title " + head });
  T(slide, body, { x: cx + 0.25, y: y + 0.8, w: cw - 0.5, h: h - 1.0, fontSize: 14, objectName: "Card text " + head });
});

// 6 runs
s = add("Light, eyebrow and title", S2);
s.addText("RUN TO RUN", { placeholder: "eyebrow" });
s.addText("Each model stayed close to itself", { placeholder: "title" });
twoCards(s, [["Rewrites", "A replication repeated the first three models’ runs minutes later. Blockers and substance checks matched the main run in every cell but one."], ["Review task", "One replication cell moved: Haiku 5.5 found 11.8 of 12 planted violations on average (11 to 12)."]], 2.45, 1.95);
T(s, "The one rewrite cell that differed is not a style difference. More on that later.", { x: X, y: 4.7, w: W, h: 0.5, fontSize: 16, objectName: "Runs note" });
s.addNotes("We also repeated the first three models’ runs a few minutes later, to see how much a model varies from itself. Very little: every rewrite cell matched the main run on blockers and substance, except one, and that one turns out not to be about writing at all. In the review task, one replication cell moved slightly: Haiku averaged 11.8 instead of 12.");

// 7 baseline
s = add("Dark, eyebrow and title", S3);
s.addText("THEN WE TOOK THE STANDARD AWAY", { placeholder: "eyebrow" });
s.addText("Same models, same passages, one line of prompt", { placeholder: "title" });
s.addText("You edit technical documentation.", { x: X, y: 2.8, w: W, h: 0.75, shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.08, fill: { color: "1F2B3A" }, fontFace: MONO, fontSize: 18, color: C.accent4, margin: [0, 18, 0, 18], valign: "middle", isTextBox: true, objectName: "Baseline prompt" });
[["HB1", "More scanner blockers without the standard"], ["HB2", "The standard costs no substance relative to none"], ["HB3", "A distractor flagged without the standard"], ["HB4", "Human meaning scores differ on inputs 02 or 03"]].forEach(([k, v], i) => {
  T(s, [{ text: k + " ", options: { bold: true } }, { text: v }], { x: X + (i % 2) * 5.95, y: 3.9 + Math.floor(i / 2) * 0.6, w: 5.6, h: 0.5, fontSize: 14, color: "BCC6D3", objectName: k });
});
s.addText("Hypotheses written before the run", { placeholder: "footer" });
s.addNotes("Then we took the standard away. Same five models, same passages, same runner, and a system prompt of one neutral line: “You edit technical documentation.” No rules, no skills. Before running it we wrote down four hypotheses: more blockers without the standard; the standard costs no substance compared with nothing; a model flags correct text when it has no rule list; and human meaning scores differ on the two hardest inputs.");

// 8 no blockers
s = add("Accent statement", S3);
T(s, "SURPRISE · HB1 NOT SUPPORTED", { x: X, y: 1.45, w: W, h: 0.32, fontSize: 12, bold: true, charSpacing: 2, color: "D6E2F8", objectName: "Eyebrow" });
T(s, "No standard, still no blockers", { x: X, y: 1.9, w: W, h: 1.9, fontFace: THEME.headFontFace, fontSize: 60, bold: true, color: C.background1, objectName: "Title" });
T(s, "All 150 baseline rewrites: no dashes, no buzzwords, no flagged phrases.", { x: X, y: 4.0, w: W, h: 0.5, fontSize: 22, color: "E4ECFA", objectName: "Finding" });
T(s, "A scanner that passes everything can’t tell you what your standard is doing.", { x: X, y: 4.7, w: W, h: 0.5, fontSize: 16, color: "D6E2F8", objectName: "Point" });
s.addText("Checked against the raw text, not only the scores", { placeholder: "footer" });
s.addNotes("Our first baseline hypothesis failed. Without any standard, every model still produced zero scanner blockers on every input. I didn’t trust the scores, so we checked the raw text of all 150 rewrites: no em dashes, no buzzwords, none of the flagged phrases. On these passages, just asking for clear technical documentation removed everything the scanner looks for. Which means the scanner, on its own, can’t show you what your standard is doing.");

// 9 precision
s = add("Light, eyebrow and title", S3);
s.addText("WHAT THE STANDARD BOUGHT · HB2 AND HB3 SUPPORTED", { placeholder: "eyebrow" });
s.addText("Substance kept, correct text left alone", { placeholder: "title" });
const hdr = (t) => ({ text: t, options: { bold: true, fill: { color: "E3E9F2" } } });
s.addTable([
  [hdr("Measure"), hdr("With standard"), hdr("Without")],
  ["Substance checks lost, input 06, per run", "0", "about 1, every model"],
  ["Planted violations found, of 12", "12", "9.0 to 10.6"],
  ["Distractors flagged, of 4", "0", "2.6 to 3.4"],
], { x: X, y: 2.45, w: W, colW: [6.0, 2.778, 2.778], fontFace: THEME.bodyFontFace, fontSize: 16, color: C.text1, rowH: 0.55, valign: "middle", margin: [4, 8, 4, 8], border: { type: "solid", pt: 0.75, color: C.accent6 }, objectName: "Comparison table" });
T(s, "The two prompts differ in more than the rule list, so this shows the difference, not which part of the prompt caused it.", { x: X, y: 4.9, w: W, h: 0.75, fontSize: 14, objectName: "Caution" });
s.addText("Ranges are across the five models", { placeholder: "footer" });
s.addNotes("So what did the standard buy? Two things the scanner can’t see. Substance: with the standard nothing was lost; without it, every model lost about one substance check per run on the code-and-flag passage. And review precision: with the rule list, every model found all 12 planted problems and flagged none of the correct text. Without it, they found 9 to 10.6 and flagged 2.6 to 3.4 of the 4 distractors. I reviewed those flags by hand and they stand. One caution: the two prompts differ in more than the rule list, so this shows the difference, not which part of the prompt caused it.");

// 10 shape
s = add("Light, eyebrow and title", S3);
s.addText("WHAT THE STANDARD BOUGHT", { placeholder: "eyebrow" });
s.addText("Shape: the page stayed a paragraph", { placeholder: "title" });
stats(s, [["2.4 → 1.9", "reads naturally, 1 to 3, blind human score (60 guided, 60 baseline)"], ["0.5 to 2.1", "headings added per baseline rewrite, by model (guided: 0 to 0.3)", C.accent2]], 2.45, 48);
eyebrowLabel(s, "Editor’s notes, written blind", X, 4.6, W, C.accent5, "Notes label");
T(s, "“Way too many headers” · “order of information changed” · “Unecessary headings and unecessary bolding” [sic]", { x: X, y: 5.0, w: W, h: 0.8, fontFace: MONO, fontSize: 14, objectName: "Notes" });
T(s, "Meaning went the other way: yes / partly / no 41 / 17 / 2 guided, 46 / 12 / 2 baseline. The standard bought shape, not meaning.", { x: X, y: 5.95, w: W, h: 0.6, fontSize: 14, color: C.text1, objectName: "Meaning result" });
s.addText("Heading counts from the structure check, added after the runs", { placeholder: "footer" });
s.addNotes("The biggest thing the standard bought was shape. In blind scoring, the guided rewrites averaged 2.4 out of 3 for reading naturally; the baseline 1.9. My notes on the baseline sheets were mostly the same complaint: too many headers, information reordered, extra bolding. Nothing in our original kit measured structure, so we added a structure check after the runs. It found the baseline adding half a heading to two headings per rewrite, depending on the model, against almost none with the standard. Because it was added after the runs, treat it as exploratory. One thing the standard did not buy: meaning. On meaning, the baseline scored the same or slightly better, mostly because of the product-name passage.");

// side-by-side example helper
const sideBySide = (slide, origLabel, origRuns, rewLabel, rewText, rewSize, h) => {
  const lw = 4.95, rw = 6.44, rx = X + lw + 0.167, y = 2.45;
  card(slide, X, y, lw, 2.65, "Box original");
  eyebrowLabel(slide, origLabel, X + 0.25, y + 0.22, lw - 0.5, C.accent5, "Label original");
  T(slide, origRuns, { x: X + 0.25, y: y + 0.6, w: lw - 0.5, h: 1.9, fontSize: 13, lineSpacingMultiple: 1.1, objectName: "Text original" });
  card(slide, rx, y, rw, h, "Box rewrite");
  eyebrowLabel(slide, rewLabel, rx + 0.25, y + 0.22, rw - 0.5, "A04E12", "Label rewrite");
  T(slide, rewText, { x: rx + 0.25, y: y + 0.6, w: rw - 0.5, h: h - 0.75, fontFace: MONO, fontSize: rewSize, color: C.text1, lineSpacingMultiple: 1.05, objectName: "Text rewrite" });
};

// 11 example B
s = add("Light, eyebrow and title", S3);
s.addText("EXAMPLE B · STRUCTURE ADDED", { placeholder: "eyebrow" });
s.addText("Four sentences became five sections", { placeholder: "title" });
sideBySide(s, "Original, input 02", "You can create maintenance plans to suppress alerts during planned work. You’ll see the plan appear in the list once you save it, and you can stop it early if you need to. You need Admin permissions to create or edit a maintenance plan. You may want to notify your team before you start a plan.",
  "Baseline · Opus 4.7, run 1", "# Maintenance Plans\nMaintenance plans suppress alerts during planned work.\n## Permissions\nAdmin permissions are required to create or edit a maintenance plan.\n## Creating a Plan\nAfter you save a maintenance plan, it appears in the list of plans.\n## Stopping a Plan\nYou can stop a maintenance plan before its scheduled end time.\n## Recommended Practice\nNotify your team before starting a maintenance plan.", 11, 3.45);
T(s, "Scored: meaning yes, reads naturally 1, “Way too many headers”.", { x: X, y: 6.02, w: W, h: 0.35, fontSize: 14, objectName: "Score" });
s.addText("Cell: Opus 4.7, input 02, baseline, 5 runs · 4.6 headings added per rewrite · guided cell: 0", { placeholder: "footer" });
s.addNotes("Here’s the structure problem in one picture. Input 02 is a four-sentence paragraph. Without the standard, Opus 4.7’s first run turned it into a page with five headings and one sentence under each. Every fact survived, so I scored meaning as preserved, but it reads like a form, and I gave it the lowest naturalness score. That wasn’t a one-off: across its five runs this model added 4.6 headings per rewrite on this input. With the standard: none. Blank lines between the markdown lines are left out here to fit the slide.");

// 12 example C
s = add("Light, eyebrow and title", S3);
s.addText("EXAMPLE C · ORDER CHANGED", { placeholder: "eyebrow" });
s.addText("The caveat moved to the end", { placeholder: "title" });
sideBySide(s, "Original, input 01", [{ text: "Correlation patterns group related alerts into a single incident. " }, { text: "Changes to a pattern apply to new alerts only — existing incidents keep their current grouping until they resolve.", options: { bold: true } }, { text: " You can edit a pattern at any time from the Correlation page." }],
  "Baseline · Opus 5.5, run 2", "## Correlation patterns\nCorrelation patterns group related alerts into a single incident.\n### Editing a pattern\nYou can edit a correlation pattern at any time from the **Correlation** page.\n> **Note:** Pattern changes apply only to new alerts. Existing incidents keep their current grouping until they are resolved.", 12, 2.65);
T(s, "Scored: meaning partly, reads naturally 1, “Reordered information breaks continuity”.", { x: X, y: 5.35, w: W, h: 0.35, fontSize: 14, objectName: "Score" });
s.addText("Human cell: Opus 5.5, input 01 · guided 2 yes · baseline 1 yes, 1 partly", { placeholder: "footer" });
s.addNotes("Example C is about order. In the original, the caveat sits right after the definition: changes apply only to new alerts. Without the standard, Opus 5.5’s second run added two headings and moved the caveat to the end, into a Note under the editing section. All the words are there; the reader just meets the warning after the instruction it qualifies. I scored it partly preserved. In this cell the two guided rewrites were both scored yes.");

// 13 automated miss
s = add("Light, eyebrow and title", S4);
s.addText("WHAT OUR INSTRUMENTS MISSED", { placeholder: "eyebrow" });
s.addText("Automated checks miss what editors see", { placeholder: "title" });
stats(s, [["0", "substance checks lost by guided rewrites on inputs 02, 03 and 04"], ["29 of 49", "sampled guided rewrites of those inputs scored “partly” or “no” by the editor", C.accent2]], 2.45, 48);
T(s, "The structure check’s heading count tracked the editor’s notes: 3.6 headings added on the 12 sheets noted for headings, 0.7 on the other 48. Its order measure caught 3 of the 6 sheets noted for reordering.", { x: X, y: 4.65, w: W, h: 1.0, fontSize: 16, objectName: "Structure check note" });
s.addNotes("This is the slide I’d most like people to remember. On inputs 02 to 04, the substance checks said the guided rewrites lost nothing. I scored 29 of the 49 sampled ones as only partly preserving meaning, or not at all. String checks look for a fact; they don’t notice when the fact’s weight or position changes. When we added the structure check afterwards, its heading count matched my blind notes closely. Its order measure is weaker: it caught three of the six sheets I’d noted for reordering, because a heavily restructured rewrite leaves fewer sentences to line up.");

// 14 harness
s = add("Dark, eyebrow and title", S4);
s.addText("EXAMPLE D · THE HARNESS IS PART OF THE PROMPT", { placeholder: "eyebrow" });
s.addText("Asked for a procedure, it returned its own environment", { placeholder: "title" });
s.addText("# Environment\nYou have been invoked in the following environment:\n- Primary working directory: [redacted]\n- Platform: [redacted]", { x: X, y: 2.65, w: W, h: 1.45, shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.08, fill: { color: "1F2B3A" }, fontFace: MONO, fontSize: 14, color: C.accent4, margin: [12, 18, 12, 18], valign: "top", isTextBox: true, objectName: "Leaked block" });
T(s, "Replication, Haiku 5.5, input 05, runs 3 and 4. Runs 1, 2 and 5 of the same cell are clean four-step procedures.", { x: X, y: 4.35, w: W, h: 0.8, fontSize: 16, color: "BCC6D3", objectName: "Where" });
T(s, "The only substance losses in the guided set: 2 of 455 scored calls. Neither was in the human sample.", { x: X, y: 5.25, w: W, h: 0.8, fontSize: 16, color: C.background1, objectName: "Impact" });
s.addNotes("Remember the one replication cell that didn’t match? Here it is. We asked Haiku to rewrite a four-step procedure. In two of five runs it returned the environment block that Claude Code, the tool running the test, adds to every call: working directory, platform, and so on. The other three runs were clean procedures. Those two outputs are the only substance losses in the whole guided set. The reader is a model, and it reads everything it’s handed, including context nobody wrote for it. Log what your harness adds.");

// 15 instruments
s = add("Light, eyebrow and title", S4);
s.addText("EXAMPLE E · OUR OWN INSTRUMENTS WOBBLED", { placeholder: "eyebrow" });
s.addText("Same sentence, two scores, one day apart", { placeholder: "title" });
quote(s, "Guided · Opus 5.5, run 4 · scored partly", C.accent5, "Use it to include change data in root cause analysis and to link deployments to the incidents they cause.", 2.45, 1.3, { size: 14 });
quote(s, "Baseline · Opus 5.5, run 1 · scored yes", C.accent5, "Use these events to include change data in root cause analysis and to link deployments to the incidents they cause.", 3.9, 1.3, { size: 14 });
T(s, "HB4 came out supported on input 03 only (guided 0/9/1, baseline 9/1/0 yes/partly/no). With rewrites this close, the difference may be the scorer. Also disclosed: the review scorer matches quotes by text, which hid at least three extra flags on one sentence.", { x: X, y: 5.4, w: W, h: 0.9, fontSize: 14, objectName: "Caveat" });
s.addNotes("Our instruments wobbled too, and I want to show that rather than hide it. These two sentences from input 03 differ by two words. I scored the first, from the guided run, as only partly preserving meaning, and the second, from the baseline run a day later, as fully preserving it. Input 03 is the only place our fourth baseline hypothesis came out supported, so that result may be my scoring drifting, not the models. There was also a scorer quirk in the review task: it matches quotes by text, whatever rule the model cites, and that hid at least three extra flags on one sentence. Both are kept as scored and disclosed.");

// 16 scoreboard
s = add("Light, title only", S5);
s.addText("Scoreboard: eight hypotheses, written first", { placeholder: "title" });
const band = (cells) => cells.map((t) => ({ text: t, options: { fill: { color: "EAEEF3" } } }));
s.addTable([
  [hdr("Hypothesis"), hdr("Result")],
  ["H1 Rule compliance costs substance (01, 02)", "Not supported"],
  ["H2 Run-to-run variation on 2+ inputs", "Not supported: one cell, the harness leak"],
  ["H3 Models differ on 03 and 04", "Not supported: 2 of 40 runs differed on 04"],
  ["H4 Models differ in review; a distractor flagged", "Not supported"],
  band(["HB1 More blockers without the standard", "Not supported"]),
  band(["HB2 Standard costs no substance vs none", "Supported"]),
  band(["HB3 Distractor flagged without the standard", "Supported"]),
  band(["HB4 Human meaning differs on 02 or 03", "Supported on 03 only; weak"]),
], { x: X, y: 1.75, w: W, colW: [6.0, 5.556], fontFace: THEME.bodyFontFace, fontSize: 14, color: C.text1, rowH: 0.42, valign: "middle", margin: [3, 8, 3, 8], border: { type: "solid", pt: 0.75, color: C.accent6 }, objectName: "Scoreboard table" });
T(s, "With the standard, the models agreed more than predicted. Differences between models within the baseline were not tested.", { x: X, y: 5.75, w: W, h: 0.6, fontSize: 14, objectName: "Scoreboard summary" });
s.addNotes("Here’s the full scoreboard. All four guided hypotheses came out false, and that’s the headline: with the standard, the models agreed more than we predicted. The guided run had no substance cost, almost no run-to-run variation, and no distractor flags. The baseline hypotheses split: no extra blockers, but the standard did protect substance and review precision, and the human meaning difference shows up only on input 03, where it may be my scoring. We didn’t test differences between models within the baseline, so no claims there.");

// 17 takeaways
s = add("Light, title only", S5);
s.addText("What to take back to your team", { placeholder: "title" });
[["Your standard is a prompt.", " Test it like one: same inputs, several runs, several models."],
 ["Say what not to change.", " In these runs, the guided prompt lost no substance and flagged no correct text; the baseline did both."],
 ["Check structure, not only words.", " The scanner found nothing in either condition; the editor found plenty."],
 ["Keep a blind human pass.", " Two rewrites per cell showed the structure problem; it could not rank anything."],
 ["Log what the harness adds.", " Two of 455 scored outputs were the harness talking."]].forEach(([b, r], i) => {
  const y = 2.0 + i * 0.85;
  T(s, String(i + 1), { x: X, y: y - 0.05, w: 0.45, h: 0.5, fontFace: THEME.headFontFace, fontSize: 22, bold: true, color: C.accent1, objectName: "Number " + (i + 1) });
  T(s, [{ text: b, options: { bold: true } }, { text: r }], { x: X + 0.6, y, w: W - 0.6, h: 0.75, fontSize: 16, color: C.text1, objectName: "Takeaway " + (i + 1) });
});
s.addNotes("Five things to take back. First, if a model reads a style standard, that standard is a prompt, so test it like one. Second, write rules that say what not to change, not only what to fix. Third, check structure; our scanner found nothing in either condition, and the problems were all in shape. Fourth, keep a blind human pass, and be honest about what a small sample can and can’t show. And fifth, log everything, including what your tooling adds to the prompt.");

// 18 close
s = add("Dark statement", S5);
T(s, "Thank you", { x: X, y: 2.1, w: W, h: 0.9, fontFace: THEME.headFontFace, fontSize: 48, bold: true, color: C.background1, objectName: "Title" });
T(s, "Kit, raw logs, scorers and pre-registrations: [link to the kit]", { x: X, y: 3.25, w: W, h: 0.5, fontSize: 18, color: "BCC6D3", objectName: "Materials" });
T(s, "Limits: small n, six passages, one review draft, runs through Claude Code with its defaults, one human scorer. These models on these inputs; not a ranking.", { x: X, y: 3.95, w: W, h: 0.8, fontSize: 14, color: "9AA6B6", objectName: "Limits" });
s.addText("Kathryn Collins · kcollins@bigpanda.io", { placeholder: "footer" });
s.addNotes("Thank you. Everything is available at the link: the pre-registrations, every raw call, the scorers, and the blind sheets. The limits matter: a small number of runs, six passages, one review draft, one human scorer, and every call went through Claude Code with its default settings. So the claim is narrow: these models, on these inputs, behaved like this. Happy to take questions.");

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
