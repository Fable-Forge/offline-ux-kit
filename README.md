[English](README.md) | [简体中文](README.zh-CN.md)

# Offline UX Kit

Local UX evidence for offline HTML and static web prototypes. An agent skill plus a dependency-free recorder, self-contained reports and two examples.

**Status: beta developer preview.** Node tests pass; real-browser file://, visual layout and Windows acceptance are pending. Do not interpret unit-test coverage as production certification.

<p align="center">
  <a href="https://github.com/Fable-Forge/offline-ux-kit/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Fable-Forge/offline-ux-kit?style=social"></a>
</p>

<p align="center">
  <strong>If this skill helps you ship better work, a ⭐ Star is free and helps others find it.</strong>
</p>

## Quick install

Give this instruction to an Agent with command-line access:

```text
Install offline-ux-kit: https://raw.githubusercontent.com/Fable-Forge/offline-ux-kit/main/docs/install.md
```

Or use the Agent Skills CLI:

```bash
npx skills add Fable-Forge/offline-ux-kit
```

See [install](docs/install.md), [update](docs/update.md), and [uninstall](docs/uninstall.md) for lifecycle instructions.

## Try without installing

Unzip the package and open `dist/form.html` in a normal browser window. Consent, select options, go back/change, record feedback and finish to download an HTML report. Try `dist/dialogue.html` for a small branching conversation. No API, account, CDN or server is needed by either example.

Open `dist/review.html` and import reports or JSON files. Use the cohort selector to keep app/build/batch/variant separate. Open `dist/sample-report.html` for a **synthetic**, not real-tester, report.

Your browser decides download behavior and local storage availability. File origins and private mode vary between browsers; inspect persistence warnings. The kit does not upload data, but reports contain behavioral evidence and should only be shared with authorized recipients.

## What is included

- `SKILL.md`, `agents/`, `references/`: AI-assisted integration workflow and constraints.
- `assets/offline-ux.js`: recorder, storage fallback, sanitizer, summary, HTML generator and importer.
- `examples/demo.html`: shared form/dialogue source.
- `scripts/build.cjs`: generate standalone demos, reviewer and synthetic report.
- `tests/core.test.cjs`: deterministic contract tests.
- `docs/`: Chinese/English knowledge articles and release acceptance record.
- `dist/`: ready-to-open standalone outputs.

## Develop

Use Node.js 18 or newer. Packaging and its regression test also require Python 3. No npm dependencies or install step:

```sh
node scripts/build.cjs
node --test tests/core.test.cjs
python tests/package.test.py
python scripts/package.py ../offline-ux-kit.zip
```

Runtime API and privacy requirements: [integration](references/integration.md), [schema](references/schema.md), [acceptance](references/privacy-and-acceptance.md).

## Use as an agent skill

Ask your coding agent to read `SKILL.md` from the extracted folder, inspect your app and produce an event map before editing. Explicit example request:

> Use the offline-ux-kit skill in this folder to instrument my existing offline three-step form. Preserve behavior, do not send data externally, and add a self-contained report. Report browser tests separately from unit tests.

The archive is not an installer and does not auto-register or enable the skill. If you later want discovery, copy the complete folder into your agent's user-specified skills location using that agent's supported installation flow. No automatic publishing is included.

## Scope and honest limits

Built-in: tasks/steps, choice/back-change, reply length, categorized feedback, estimated active/hidden time, interrupted sessions, optional AI request metadata, rapid clicks, JSON/HTML/Markdown, ordered session funnel, dwell bars, issue donut, selection counts and event table. The report interface mixes Chinese and English; documentation is fully bilingual, the UI is not fully localized.

Not built in: video/DOM replay, screenshots, lobby maps, native desktop/mobile apps, long-term analytics backend, free-text feedback, old private The Closer v2 conversion, automatic integration into arbitrary frameworks, or side-by-side cohort comparisons. Task paths are event evidence, not screen recordings. There is no CSV export.

Storage rewrites session snapshots; appropriate for lightweight tests, not high-volume telemetry. Multiple tabs writing one session are unsupported. Shutdown can lose pending writes. Idle cutoff is an estimate and undercounts long reading. Review [validation status](docs/VALIDATION.md) before release.

## License

MIT, copyright 2026 FableForge. Third-party apps adapted with the skill retain their own licenses. Both examples are original, no The Closer source or company assets are included.
