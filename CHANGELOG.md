# Changelog

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## 2026-09-25

### Added
- A real `Docs` CI badge (the `docs.yml` link-check workflow, which actually
  runs — unlike a fake "tests passing" badge this repo can't honestly claim)
  and a `scenarios-140` badge to the README badge row.

## 2026-09-24

### Fixed
- README's "What's in here" table still said "15 Gherkin feature files" after
  yesterday's `KeyboardAndFocus.feature` addition brought it to 16 — the
  headline "~140 scenarios across 16 feature files" line was already correct,
  this was a second, missed mention.

## 2026-09-23

### Added
- `KeyboardAndFocus.feature` (12 scenarios): Tab order through the entry form,
  derived from `MainForm.Designer.cs`'s real `Controls.AddRange` order (Labels
  are not tab stops) rather than guessed — documented in `NameMapping.md`.
- `BaseScreen.focus` / `.is_focused` / `.press_key` primitives.
- Registered in `ContactManager.mds`; every step verified to resolve to exactly
  one `KeyboardAndFocusSteps.py` routine, including every Examples row.

## 2026-09-22

### Added
- Cancel superseded CI runs on the same branch (`concurrency` group in the workflow).

## 2026-09-19

### Added
- `.gitattributes` normalizing line endings across C#, docs and scripts.

## 2026-09-16

### Added
- Dependabot for the SUT's NuGet packages and `github-actions`.

## 2026-09-13

### Added
- `SECURITY.md`.

### Fixed
- `SECURITY.md` issues link now uses the absolute GitHub URL (a relative
  `../../issues/new` resolved outside the repo and would fail the link check).

## 2026-09-08

### Added
- Offline Markdown link-check CI workflow (`.github/workflows/docs.yml`) — the
  only thing this doc-heavy, non-runnable showcase can verify automatically.

## 2026-09-07

### Added
- `scripts/merge-logs.md`, detailing the "collect and merge" step from
  `docs/DISTRIBUTED-EXECUTION.md`.

## 2026-09-06

### Added
- `.github/ISSUE_TEMPLATE/{bug_report,flaky_test}.md` and
  `.github/pull_request_template.md`.

## 2026-09-05

### Added
- `runners.yml` — a module→runner ownership manifest, the concrete shape the
  "keep ownership in the repo" advice in `DISTRIBUTED-EXECUTION.md` takes.

## 2026-09-03

### Added
- `CONTRIBUTING.md` (layering rules, what can be verified without a
  TestComplete/TestExecute license).

## 2026-09-02

### Added
- SUT: contacts gain phone, category and favourite fields; category/favourite
  filtering; sort control; File > New list and Export to CSV; About dialog
  version bump.
- Screens: `BaseScreen` combo-box/checkbox primitives, `MainScreen` actions for
  edit/filter/sort/export, `ExportDialog`, `AboutDialog` version query.
- BDD: feature coverage for add/edit/delete, validation, duplicate email, phone
  format, search, category filter, sort, count label, export, new list, status
  messages and About — one step definition module per area.
- `.claude/` agents (`screen-object-author`, `namemapping-reviewer`,
  `scenario-triager`) and skills (`new-feature-coverage`, `bdd-step-audit`).
- `CLAUDE.md`, `NameMapping.md`, the feature map and the expanded README.

## 2026-08-31

### Added
- Initial scaffold: `BaseScreen`, explicit waits, config and scenario hooks;
  `MainScreen` and `AboutDialog` screen objects; Add/Delete/Search/About
  features with thin step definitions.
- `docs/SCREEN-OBJECT-MODEL.md`, `docs/BDD-INTEGRATION.md`,
  `docs/DISTRIBUTED-EXECUTION.md`.
- Repository overview and the "pattern showcase, no proprietary code"
  disclaimer.
