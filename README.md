# Creator Continuity

Every new AI chat can feel like starting with a different assistant.

A creator may preserve the draft text but lose the deeper continuity: audience, taste, style, canon, causal memory, external context, unresolved questions, and the reason the work exists.

Creator Continuity Record is a small handoff structure for preserving creative continuity across AI sessions. It helps the next AI reconnect to Aspire, audience, style, canon, causal memory, unresolved items, next move, and what it must not change.

Creator Continuity does not only preserve style. It preserves Aspire: the reason the style exists.

## Start In 3 Minutes

1. Copy [examples/blank-record-template.json](examples/blank-record-template.json) beside your draft or notes.
2. Fill in Aspire, audience, style, canon, current_state, the best-known state of the work, failure patterns, next_move, and next_ai_should_not.
3. Paste the record into a new AI chat with [docs/prompt-for-creative-agents.md](docs/prompt-for-creative-agents.md).

This is prompt-first. You do not need automation, a bot, analytics, or a publishing workflow to use it.

## What This Is

- A restartable continuity record for creators working across AI chats.
- A way to preserve audience, taste, canon, intent, and open questions.
- A local, prompt-first artifact that can live beside drafts, notes, scripts, newsletters, essays, or campaign material.
- A check-only structure: it helps decide whether a handoff is ready, paused, or blocked.

## What This Is Not

- Not a content generator.
- Not a posting bot.
- Not an analytics platform.
- Not a revenue predictor.
- Not a scraper for external platforms.
- Not a guarantee of perfect identity, taste, or style preservation.
- Not a replacement for human creative judgment.
- Not an engagement-optimization system by default.
- Not a scoring, weighting, or threshold system for creator taste.
- Not an autonomous publishing workflow.

## Core Idea

A Creator Continuity Record answers:

1. What is this work trying to become?
2. Who is it for?
3. What must remain true?
4. What changed since the last record?
5. What is unresolved?
6. Where should the next AI begin?
7. When should the next AI stop instead of continuing?
8. What should the next AI avoid changing?

## Continuity Status

`continuity_status` has three values:

- `READY`: The record is restartable enough for the next AI session.
- `PAUSE`: The record is missing context, but the missing context can likely be supplied.
- `BLOCK`: Continuing would risk breaking audience trust, canon, facts, creator intent, or public-facing constraints.

`READY` is not a quality guarantee. It does not mean the content is good, finished, on-brand, factual, or ready to publish. It only means the continuity record gives the next AI enough context to resume without inventing the direction.

`PAUSE` and `BLOCK` are valid integrity-preserving outputs. They protect the creator from smooth-sounding drift.

## Minimal Record

See [creator_continuity_record.schema.json](creator_continuity_record.schema.json) for the schema.

The main fields are:

- `as_of`
- `project_name`
- `aspire`
- `audience`
- `creative_intent`
- `current_state`
- `what_changed`
- `canon`
- `style`
- `taste`
- `causal_memory`
- `external_context`
- `reference_anchor`
- `open_questions`
- `next_move`
- `stop_condition`
- `reanchor_condition`
- `next_ai_should_not`
- `continuity_scope`
- `continuity_status`
- `handoff_prompt`
- `notes`

## Examples

Creator Continuity is not only for writers. It can preserve continuity for image series, short video formats, newsletters, essays, threads, campaigns, and brand work.

- [Blank template](examples/blank-record-template.json): copy-paste starting point for a new project.
- [Agentic creator workflow](examples/agentic-creator-workflow.json): bounded long-running agent work without creative drift.
- [Food essay](examples/food-essay.json): sensory food writing without flattening the creator's taste.
- [Image series creator](examples/image-series-creator.json): character, visual taste, palette, and composition continuity.
- [Newsletter creator](examples/newsletter-creator.json): recurring newsletter continuity across issues.
- [Short video creator](examples/short-video-creator.json): format, pacing, hook, and rhythm continuity.
- [X thread creator](examples/x-thread-creator.json): thread continuity without engagement-bait drift.

## Prompt-First Usage

Before asking a new AI chat to continue a creative project:

1. Write or update a Creator Continuity Record.
2. Include links or paths to real reference anchors.
3. Mark unresolved questions instead of smoothing them away.
4. Set `continuity_status` honestly.
5. Paste the `handoff_prompt` into the next session with the record.

See [docs/prompt-for-creative-agents.md](docs/prompt-for-creative-agents.md) for a reusable agent prompt.

## Boundary

Creator Continuity is intentionally small. It does not automate publishing, scrape platforms, judge creator identity, or optimize for metrics. Its job is narrower: preserve enough creative continuity that the next session can restart from the actual work instead of starting over with a plausible imitation.
