---
name: offline-ux-kit
description: Add local UX telemetry, categorized feedback and self-contained HTML reports to offline HTML or static web prototypes. Use for offline playtest logs, form usability tests and task paths; not native-app instrumentation or advertising analytics.
---

# Offline UX Kit

Instrument an existing browser application without changing its business decisions. Reuse `assets/offline-ux.js`; do not regenerate the recorder from scratch.

## Inspect and map

Read entrypoints, routing, completion handlers, storage and network calls. Preserve unrelated files. Identify the test variant: `offline-scripted` or `local-html-with-ai`. An HTML entrypoint alone does not mean offline.

Produce an event map: operation → stable task/step ID → exact call site → allowed metadata → completion/abandonment condition. Read [integration.md](references/integration.md) and [schema.md](references/schema.md). Extend the metadata allowlist and tests together when an adapter needs new fields.

## Integrate

Copy or inline the runtime. Obtain informed test consent and an anonymous code. Use a stable per-run session ID for refresh recovery, and a new ID for new tests. Never use names, emails or input text as identifiers.

Await `OfflineUX.create()` before instrumented interaction. Call the task, step, choice, back, reply and endTask methods that correspond to real transitions in the event map; do not emit artificial events for interactions the host does not have. `data-ux-id` captures explicit clicks and rapid-click signals; it does not infer task completion.

Wire an accessible feedback selector and finish/export button. Call `endTask('completed')` only at real success. Await `finish()` before `report()`. Keep raw JSON available. Show persistence warnings; never promise recovery in memory mode. Do not delete data after export.

Read [privacy-and-acceptance.md](references/privacy-and-acceptance.md) before shipping. Do not collect input text, credentials, request bodies, URLs, error messages or imported business data. This release supports categorized feedback, not comments. Inventory host network calls; do not patch global fetch to fake offline safety.

## Report

Use `OfflineUX.report(run)` and `OfflineUX.reviewer()`. Keep builds, batches and variants separate. The generic funnel is session-level ordered reach, not task conversion. Use task-run IDs for custom task-level conversion. Missing events are missing evidence, not zero failures.

## Validate and deliver

Run `node scripts/build.cjs`, then `node --test tests/core.test.cjs` and `python tests/package.test.py` from the kit. Test the modified application separately in a real browser: completion, back/change, feedback, export, refresh, background timing, fallback, report import and hostile input. Automated tests do not validate browser persistence or visual rendering.

Deliver the modified app, reviewer, sample data and test results with unverified platforms clearly marked. Do not install, publish, upload logs or overwrite the original unless requested.
