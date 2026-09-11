# Changelog

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
