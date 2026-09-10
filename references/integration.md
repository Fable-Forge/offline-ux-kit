# Integration contract

Load assets/offline-ux.js locally or inline it. No runtime package installation is required.

```js
const ux = await OfflineUX.create({appId:'prototype', buildId:'v1', batchId:'pilot', participantId:'tester-003', sessionId:'unique-run-id', variant:'offline-scripted'});
ux.task('application');
ux.step('preferences');
ux.choice('option-a');
ux.back();
ux.step('preferences');
ux.choice('option-b');
ux.reply('Input is counted, never stored');
ux.feedback('unclear');
ux.endTask('completed');
const run = await ux.finish(4);
OfflineUX.download('experience.html', OfflineUX.report(run));
```

finish() is idempotent: close unfinished task as abandoned, freeze run, remove listeners. snapshot() exports without finishing. Reuse sessionId for refresh recovery; use distinct IDs in simultaneous tabs. Do not allow concurrent writers to the same session. After finish, start a new session ID. Storage is written only after create(), so call it after consent. Anonymous metadata cannot contain names or actual user input. Structural IDs must match [A-Za-z0-9_.:-]{1,80}; create(), task(), step(), choice() and custom track() calls reject invalid IDs instead of merging them under a placeholder.

## Timing and recovery

Refresh the warning getter after writes or poll it periodically: storage can fail after initial startup. The example polls every two seconds. If localStorage is blocked but IndexedDB works, the example cannot retain its session pointer across reload: require a tester-retained session code in a production adapter, or store the pointer in IndexedDB. Do not claim automatic resume in that condition. Batch and participant identity are immutable within one session; changed values cause an error instead of silently mixing users.

Use performance-based elapsed time, not wall clock differences. Active time stops 20 seconds after the last pointer/key/semantic action by default; this is an estimate, not attention detection. Longer reading remains visible but idle. Hidden time is separate. Heartbeats write every 5 seconds. Reload appends a new segment; closed-browser gaps are excluded. Abrupt shutdown may lose the last heartbeat and pending async writes.

Resume marks the previous unfinished task interrupted. The adapter must restart or restore its own business state; the runtime does not do this. Choice-change detection resets for the new task run. Explicitly call task() and step() after reload.

## AI integration

Call aiStart() before the host request, aiEnd(id,'success'|'error') after response, and aiFallback() when local fallback is used. The kit never makes API calls. Step exit marks pending requests ai_wait_abandon and ignores late callbacks; cancel the actual network request in the host if desired. Never pass prompts, keys or responses.

## Extension boundaries

track(name,data) accepts only allowlisted metadata. Extend code and tests for new fields. Position sampling does not automatically create a map. Lobby maps, custom task funnels, per-question decision latency, cross-version comparison charts and free-text feedback are not built into the current beta. For maps, sample at most 1 Hz with a movement threshold, never each render frame.
