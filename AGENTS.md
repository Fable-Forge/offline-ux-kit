# Repository Guidance

## Scope

These instructions apply to the entire repository.

## Source and generated files

- `assets/offline-ux.js` is the runtime source.
- `examples/demo.html` is the shared demo source.
- `scripts/build.cjs` generates `dist/`; do not edit generated HTML or sample outputs by hand.
- `SKILL.md` is the Agent workflow entrypoint. Keep detailed contracts in `references/`.

## Required checks

- Run `npm test` after runtime, demo, report, packaging, or generated-output changes.
- Run `python scripts/validate_repository.py` after repository or publication metadata changes.
- Run an available Agent Skill validator after changing `SKILL.md` or `agents/openai.yaml`.
- Keep automated checks separate from real-browser acceptance in `docs/VALIDATION.md`.

## Boundaries

- Preserve the local-only, no-automatic-upload behavior.
- Do not collect input text, credentials, request bodies, URLs, error details, or imported business data.
- Do not claim browser persistence, zero network requests, visual quality, or installation triggerability without direct evidence.
- Do not add a release number or publish a release unless the user explicitly requests it.
