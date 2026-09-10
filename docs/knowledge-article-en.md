# Understand an offline prototype before it goes online

A tester says a prototype feels confusing. That is useful feedback, but it does not tell you whether they missed the entry point, misunderstood an instruction, changed their mind, or waited for an unresponsive control. Completion scores alone cannot explain the path.

Offline UX Kit adds local behavioral evidence to HTML and static web prototypes. At the end of a session, the tester exports a self-contained HTML report. The workflow does not require an analytics backend, an account or a hosted dashboard.

## Start with questions, not click volume

Useful questions include whether the tester reached the main task, which steps involved long pauses or backtracking, where they abandoned the task, and what happened before categorized feedback. For AI-assisted applications, request latency and fallback can also matter.

These questions apply to training, forms, questionnaires, interactive demonstrations and small browser experiences. That is why the shared model uses tasks, steps, actions and outcomes instead of game-specific concepts.

A registration form and a branching customer conversation have different content, but both contain transitions, choices, revisions and completion conditions.

## An agent skill and a tested library serve different jobs

The skill instructs a coding agent to inspect an existing application, identify semantic transitions and produce an event map. The library supplies consistent event ordering, timing, persistence, summaries and report generation.

The agent decides where measurement belongs; reusable code handles the mechanics. This avoids asking an agent to regenerate foundational storage and timing logic for every integration.

## Reports should carry their evidence

JSON preserves structured events, but a self-contained HTML report makes them easier to inspect. The first release includes metric cards, an ordered session funnel, step-duration bars, issue distribution, selection counts and expandable event tables. A separate reviewer imports multiple sessions and separates application, build, batch and variant cohorts.

Markdown supports summary archiving, while browser printing provides a reading snapshot. Neither replaces the raw evidence.

One session should show reached/not reached states, not pretend to establish population conversion rates. Session counts are not unique people. Different builds or AI/scripted variants should not be silently combined.

## A pause is a signal, not a diagnosis

The default active-time estimate stops twenty seconds after the last relevant action. A page may remain visible beyond that cutoff, including while someone is reading carefully. The estimate can therefore undercount reading.

Review active time alongside visible time, backtracking, changed selections and feedback. Rapid clicks suggest a place to investigate; they do not prove that a control failed. Use the report to narrow the investigation, then interpret the task and ask the tester what happened.

## Local processing still needs privacy boundaries

A downloaded report can be forwarded. Local storage alone does not make unrestricted collection appropriate.

The kit uses an explicit metadata allowlist. Replies retain length rather than content, feedback retains categories, and credentials, request bodies, imported business records and detailed errors are not collected. Report labels use text content, embedded JSON escapes script-closing characters, and imported HTML is parsed for a data block rather than executed.

An allowlist is not a secret detector. Adapters must not put a credential into an option ID or a person's name into an anonymous identifier. Explain collection and intended recipients before testing.

## Keep the first release honest

The current beta targets lightweight offline browser tests. It is not a screen recorder, native application SDK or analytics service. It does not include lobby maps, free-text feedback, migration from the older private The Closer schema, or high-volume append-only storage.

Recovering logs is also different from restoring application state. The example restarts a task after refresh and records the interrupted attempt; it excludes the closed-browser interval from active time. Abrupt shutdown may lose pending asynchronous writes.

Automated logic tests have passed for this release. Real-browser file opening, rendering and Windows acceptance remain pending. These limits must travel with the package; results from an earlier project cannot certify a new implementation.

## A practical adoption path

Choose one short core task. Ask the agent to map transitions before editing, then integrate the reusable recorder at business handlers. Test normal completion, back/change and abandonment. Inspect whether the report distinguishes those paths.

Next check refresh, background timing, storage failures, duplicate imports and hostile input. Separate code-level tests from real-browser behavior. Expand instrumentation only after the first task provides useful evidence.

The lasting value is not the chart style. It is the habit of deciding, while building the prototype, what evidence would help explain where someone gets stuck—and using that evidence to choose the next concrete product change.
