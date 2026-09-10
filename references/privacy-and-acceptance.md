# Privacy and acceptance

Explain collection, local storage, export recipients and retention. Reports remain sensitive behavior data without names. This kit does not encrypt storage. No automatic upload or deletion. Examples collect only after consent.

## Release checks

- Preserve original host behavior and source.
- Complete and abandon tasks; backtrack and change choice.
- Check unique eventId and increasing seq after refresh.
- Close/reopen using the same session in the delivery browser.
- Measure a real 15-second background interval; test idle cutoff with fake clock.
- Force IndexedDB failure, then both stores failing; display warnings.
- Finish/export/reopen HTML, inspect timeline, download JSON/Markdown.
- Import duplicates, conflicts, malformed data and hostile markup.
- Verify imported HTML is never mounted or executed.
- Monitor all host requests; pure-offline path must make zero HTTP(S) requests.
- Test file:// in Windows Chrome/Edge before claiming compatibility there.
- Test 20-session import, narrow layout, keyboard use and print.
- Scan public source for secrets, proprietary assets and machine-specific paths.

No CSV export in this release. If added, defend against spreadsheet formulas including leading whitespace/control characters. Escape `<` in embedded JSON and use textContent for report labels.

Scope: lightweight prototype sessions. Snapshots rewrite the run, events stay in memory, and tables are not virtualized. Before supporting heavy or hours-long tests, add append-only event storage, chunking and pagination. Concurrent same-session writers are unsupported. Async shutdown persistence cannot be guaranteed.
