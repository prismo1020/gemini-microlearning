# Prompt it. Slop-check it.

A public, self-contained microlearning by Danielle Beram. Learners recognize AI tells in a practice draft, build a presentation prompt, compare designs, and revise the draft using supplied facts.

## Try it

Serve this directory with any static HTTP server, or publish its root with GitHub Pages. No build, API key, Google account, or AI subscription is needed for the learning activities. External presentation generation is an optional extension.

## What learners do

1. Explore seven AI-tell examples with contextual feedback and optional hints.
2. Customize the audience and decision in a reusable presentation prompt.
3. Compare identical text in two illustrative designs and inspect a public template.
4. Choose an account-appropriate Slides, Canvas, or manual workflow.
5. Revise the draft, view local phrase-check feedback, and compare an example.
6. Download their own prompt, draft, facts, and checklist.

AI tells are the activity's focus. They are patterns to question, not proof of authorship. Phrase checks are transparent local heuristics, not a detector or mastery assessment. All business figures in the exercise are fictional.

## Original voice, optional

Five original recordings are retained byte-for-byte in `assets/audio/`: slides 01, 07, 09, 12, and 15. The Listen button and native audio controls play them only on request. Navigation never waits for audio. Transcripts and contextual notes accompany each clip. The workflow chapter has no audio because the original instructions no longer fit it. A natural next production improvement is recording that chapter in Danielle's voice.

The remaining legacy audio and deck imagery are absent from the current course tree. Earlier versions remain in Git history; this update does not rewrite history.

## Public template and comparisons

[Professional Business / Salerio by SlidesCarnival](https://www.slidescarnival.com/template/salerio-free-presentation-template/1875) is the public reference. Learners obtain a copy from its provider and retain credits under the provider's terms. The lesson does not distribute the unmodified third-party template. The in-lesson comparison is an original illustration with identical text, not captured Gemini output or an exact reproduction of the template. The optional actual-cover image is attributed and loaded from the provider.

## Workflow verification

Checked against primary documentation on October 26, 2026:

- [Generate presentations directly in Slides](https://support.google.com/docs/answer/17111393?hl=en)
- [Create and export from Gemini Canvas](https://support.google.com/gemini/answer/16047321?hl=en)
- [Import themes and use templates](https://support.google.com/docs/answer/1705254?hl=en)
- [Download Slides as PowerPoint](https://support.microsoft.com/en-gb/office/quick-tips-create-and-open-a-powerpoint-presentation-9401a8fb-a164-4d9f-97d5-9d72c1deb1a0)

Documentation was verified, not the UI of an authenticated Google account. Account, plan, language, and rollout differences are stated in the lesson. No fixed model-version recommendation is made.

## Learning design

The performance context is a leadership decision about a fictional pilot. Learners inspect actual text, receive specific feedback, and revise a usable draft. This design is informed by [Michael Allen's CCAF framework](https://blog.alleninteractions.com/talking-sam-ccaf-adaptive-learning). It does not claim endorsement or certification.

## SCORM 1.2

`prompt-it-scorm12.zip` is ready for LMS testing. Rebuild it with:

```sh
python3 build_scorm.py
```

The manifest launches `index.html` as one SCO. The adapter initializes, bookmarks the chapter, resumes the chapter, and reports `completed` only when the learner selects **Finish practice**. It never reports a mastery score. Draft text and AI-tell selections stay in browser storage and are not sent to the LMS. Target-LMS acceptance testing is still required.

## Accessibility and privacy

Audio is optional, all phrase selections are keyboard-operable buttons, feedback uses live regions, and motion respects the system preference. The lesson supports narrow screens. Progress and the draft are stored on the current device if storage is available; Reset my practice clears that state. It makes no AI API calls. Google Fonts and the optional template preview are external resources; system fonts and the self-contained challenge remain usable if they fail.
