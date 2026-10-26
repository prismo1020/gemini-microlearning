# Prompt it. Slop-check it.

A public, self-contained microlearning by Danielle Beram. Learners recognize AI tells in a practice draft, build a presentation prompt, compare designs, and revise the draft using supplied facts.

## Try it

Serve this directory with any static HTTP server, or publish its root with GitHub Pages. No build, API key, Google account, or AI subscription is needed for the learning activities. External presentation generation is an optional extension.

## What learners do

1. Review six sentences: keep useful content, flag three AI-tell examples, and revise them beside contextual feedback.
2. Customize the audience and decision, revise a flawed practice outline, and use the approved outline in the prompt.
3. Inspect the actual public template and optionally compare locally selected screenshots of real generated outputs.
4. Choose an account-appropriate Slides, Canvas, or manual workflow.
5. Judge four sentences in an independent draft before seeing feedback, then revise it and compare an example.
6. Download their own prompt, draft, facts, and checklist.

AI tells are the activity's focus. They are patterns to question, not proof of authorship. Phrase checks are transparent local heuristics, not a detector or mastery assessment. All business figures in the exercise are fictional.

## Original voice, optional

Five original recordings are retained byte-for-byte in `assets/audio/`: slides 01, 07, 09, 12, and 15. The Listen button and native audio controls play them only on request. Navigation never waits for audio. Transcripts and contextual notes accompany each clip. The workflow chapter has no audio because the original instructions no longer fit it. A natural next production improvement is recording that chapter in Danielle's voice.

The remaining legacy audio and deck imagery are absent from the current course tree. Earlier versions remain in Git history; this update does not rewrite history.

## Public template and comparisons

[Professional Business / Salerio by SlidesCarnival](https://www.slidescarnival.com/template/salerio-free-presentation-template/1875) is the public reference. Learners obtain a copy from its provider and retain credits under the provider's terms. The lesson does not distribute the unmodified third-party template. The lesson displays the actual attributed template cover. It does not substitute staged mockups for generated outputs. An optional comparison workspace accepts two local screenshots, keeps them in page memory, and never uploads them. The independent challenge and all other learning activities need no external AI account.

## Workflow verification

Checked against primary documentation on October 26, 2026:

- [Generate presentations directly in Slides](https://support.google.com/docs/answer/17111393?hl=en)
- [Create and export from Gemini Canvas](https://support.google.com/gemini/answer/16047321?hl=en)
- [Import themes and use templates](https://support.google.com/docs/answer/1705254?hl=en)
- [Download Slides as PowerPoint](https://support.microsoft.com/en-gb/office/quick-tips-create-and-open-a-powerpoint-presentation-9401a8fb-a164-4d9f-97d5-9d72c1deb1a0)

Documentation was verified, not the UI of an authenticated Google account. Account, plan, language, and rollout differences are stated in the lesson. No fixed model-version recommendation is made.

## Learning design

The performance context is a leadership decision about a fictional pilot. Guided practice mixes three useful sentences with three AI-tell examples; an em dash and a concrete three-item list are deliberately retained. Feedback distinguishes unnecessary flags from supported decisions. Edits appear in the source draft. A separate four-sentence task delays feedback until the learner submits the full set of decisions. Selecting every option or no options yields only two aligned decisions, rather than automatic completion. The final phrase checker reports patterns to inspect and does not validate meaning. This design is informed by [Michael Allen's CCAF framework](https://blog.alleninteractions.com/talking-sam-ccaf-adaptive-learning). It does not claim endorsement or certification.

## SCORM 1.2

`prompt-it-scorm12.zip` is ready for LMS testing. Rebuild it with:

```sh
python3 build_scorm.py
```

The manifest launches `index.html` as one SCO. The adapter initializes, bookmarks the chapter, resumes the chapter, and reports `completed` only when the learner selects **Finish practice**. It never reports a mastery score. Draft text, sentence decisions, edits, and outline choices stay in browser storage and are not sent to the LMS. Target-LMS acceptance testing is still required.

## Accessibility and privacy

Audio is optional, all phrase selections are keyboard-operable buttons, feedback uses live regions, and motion respects the system preference. The lesson supports narrow screens. Progress and the draft are stored on the current device if storage is available; Reset my practice clears that state. It makes no AI API calls. Google Fonts and the optional template preview are external resources; system fonts and the self-contained challenge remain usable if they fail.

## Checks

Run `node tests/check.cjs` for activity-logic and simulated LMS checks, then `python3 build_scorm.py` to rebuild the package. Browser QA covers wrong flags, inline edits, approved-outline propagation, local screenshots, independent review, original audio playback, saving, reset, kit download, and desktop/mobile layouts. Structural and software checks do not establish learning transfer.
