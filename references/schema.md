# Schema v1

This independent kit is not compatible with the earlier private The Closer schema v2. An explicit converter is required. Unsupported versions are rejected.

Envelope: {meta,events}. Reports embed an array in script[type="application/json"]#report-data. Imported HTML is read as text, never executed.

meta: schemaVersion=1, kitVersion, appId, participantId, sessionId, batchId, buildId, variant, startedAt, endedAt, storageMode. Modes: indexedDB/localStorage/memory.

Event: eventId, seq (strictly increasing), timestamp (display only), elapsedMs (monotonic segment sum), sincePreviousMs, name, taskId, taskRunId, stepId, data.

Events: run_start/resume/end, task_start/end, step_enter/exit, time_slice, choice, back, reply, feedback, signal, ai_start/end/fallback, foreground/background, click, js_error, network, survey.

Metadata allowlist: optionId, previousOptionId, changed, length, durationMs, status, code, category, reason, requestId, x, y, rating, activeMs, visibleMs, hiddenMs, count, inputMode. Only finite numbers, booleans and stable ASCII string IDs survive. Nested data, arbitrary text and unknown keys are dropped. Do not supply a credential as an allowed ID: an allowlist is not a secret detector.

Task outcomes: completed, abandoned, interrupted (on resume). Abandoned summary includes interrupted tasks. Selection counts include repeats. No inference of correctness or satisfaction.

Importer limits: 10 MiB/file, 100,000 events/run, 200 sessions. Equal appId+sessionId snapshots are skipped; conflicts are rejected, not silently overwritten. Use the latest snapshot in a fresh reviewer. Cohorts are separated by app/build/batch/variant. Metrics count sessions, not unique people.
