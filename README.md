# Prompt it. Slop-check it.

A short AI microlearning by Danielle Beram. Nine focused screens, one action at a time, and a large blue Next button throughout.

## The experience

- Spot an empty “not just X” flourish.
- Keep a useful em dash.
- Choose a concrete list over an abstract three-pack.
- Choose a usable presentation brief.
- Get the public template.
- Follow three steps in Slides, Canvas, or PowerPoint.
- Rewrite a short draft; feedback updates while typing.
- Catch an invented conclusion in a fresh example.
- Download the prompt, rewrite, facts, and review prompt.

Correct answers get green feedback. Wrong answers get yellow try-again feedback. One answer click reveals the explanation; there is no separate submit/review step. Next never waits for an answer or narration. Back preserves choices and the rewrite.

## Voice

Five original recordings remain byte-for-byte unchanged: `slide-01.mp3`, `slide-07.mp3`, `slide-09.mp3`, `slide-12.mp3`, and `slide-15.mp3`. My voice is optional, with transcripts beneath the relevant screens. The legacy “brand file” reference now means the public template, and the tone tip is already incorporated into the full prompt. No synthetic replacement voice is used.

## Public template

[Professional Business / Salerio by SlidesCarnival](https://www.slidescarnival.com/template/salerio-free-presentation-template/1875) is the public reference. Learners obtain a copy from the provider and keep its credits. The preview is the actual template cover. No staged mockups are presented as generated outputs. Learners can generate the same outline with and without the template to compare real outputs.

## Learning and privacy

The practice uses fictional pilot facts. AI tells are editing clues, not proof of authorship; that context appears in the resources, rather than interrupting each activity. The live rewrite check uses local phrase patterns and a check for the supplied numerical comparison; it is not an AI detector or factual validator. It does not assign mastery scores. The exercise follows a challenge/action/feedback pattern informed by [Michael Allen's CCAF framework](https://blog.alleninteractions.com/talking-sam-ccaf-adaptive-learning).

The draft and choices save only in this browser. No AI service receives them. Google Fonts and the attributed template preview are external resources; system fonts and the self-contained activities remain available if those resources fail.

## Workflow references

Checked October 26, 2026 against primary documentation, not an authenticated Google account:

- [Generate presentations in Slides](https://support.google.com/docs/answer/17111393?hl=en)
- [Create and export from Canvas](https://support.google.com/gemini/answer/16047321?hl=en)
- [Import a theme](https://support.google.com/docs/answer/1705254?hl=en)

Account, plan, language, and rollout details are kept in resources. Direct Slides generation is documented for eligible accounts on desktop in English. No fixed model-version recommendation is made.

## Run and package

Serve this directory with a static HTTP server or GitHub Pages. No build or API key is required.

```sh
node tests/check.cjs
python3 build_scorm.py
```

The ZIP contains the same lesson and original recordings. SCORM 1.2 initializes, bookmarks/resumes the screen, and marks participation complete when Finish is selected. No score is sent. Draft text stays on the device. Target-LMS acceptance testing remains necessary.

The earlier lesson and its removed assets remain in Git history. This update does not rewrite history.
