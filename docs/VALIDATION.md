# Validation / 验收记录

Status: beta developer preview. Date: 2026-09-10.

## Passed / 已通过

- 30 Node contract tests via `node --test tests/core.test.cjs`.
- Portable ZIP regression via `python tests/package.test.py`: one generated manifest, no duplicate paths and byte-identical source files.
- Deterministic fake-clock active/visible/hidden and idle accounting.
- Choice changes, backtracking, task completion/abandonment, interruption on resume.
- Input-text exclusion and allowlisted metadata.
- AI duration, abandonment and fallback accounting (no real API call).
- Idempotent finish; post-finish calls cannot write to a closed store.
- Mocked localStorage fallback and memory-only warning.
- Schema/order/unique-event validation, malformed metadata rejection.
- Embedded JSON script escaping and import without HTML execution.
- 20-report import, duplicate detection, atomic conflict rejection.
- Inline JavaScript syntax checks in both generated HTML demos.
- Skill frontmatter validator.
- Independent three-step integration in Node: choose → review → submit, back/change, feedback, final report and interruption recovery. Findings were fixed and covered by regressions.

## Not verified / 待验收

The current cloud browser rejected local file:// navigation under its URL security policy. No alternate browser surface or indirect route was used. Consequently:

- No real-browser render or screenshot QA.
- No actual IndexedDB browser transaction/reopen test.
- No actual browser download/reopen/import interaction test.
- No real 15-second background test.
- No live network trace; source contains no runtime network calls and examples use restrictive CSP, but this is not measured zero-request evidence.
- No Windows Chrome/Edge, mobile layout, keyboard-only or print acceptance.

The source and generated files are a preview, not a browser-certified release. Do not cite the older project's 12/19 or 37/37 results for this build.

## Manual handoff / 回家后验收

1. Extract the archive in a normal folder. Open dist/form.html in Chrome.
2. Consent, choose design, advance, back, choose engineering, finish the remaining steps.
3. Record feedback; export HTML and JSON. Verify a changed choice and completion in the report.
4. Start a new test, switch tabs for 15 seconds, return and export. Check hiddenMs.
5. Start another test, refresh with the same anonymous code, then finish. Confirm interrupted prior task and unique seq.
6. Close/reopen before finish; confirm saved evidence is retained. Allow time for the heartbeat before closing.
7. Import identical reports twice in dist/review.html. Check duplicate count. Import a corrupted JSON and confirm readable error.
8. In developer tools, verify no HTTP(S) request over the complete offline path. Repeat in Edge.
9. Check keyboard navigation, narrow window layout and printing.

If any check fails, retain the failing report plus browser/version and reproduction steps. Never attach credentials or private source data.
