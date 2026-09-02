# CLAUDE.md — working agreement for AI agents in this repo

This project is developed with an **agentic-AI workflow**: Claude Code and the
subagents/skills in `.claude/` draft screen objects, step definitions and feature
files, review NameMapping intent, and triage failing scenarios against the
conventions below.

## What this project is

| | |
|---|---|
| Tool | SmartBear **TestComplete 15+** (Desktop + Python modules) |
| SUT | `sut/` — **Contact Manager**, a small .NET 8 WinForms app, the only automation target |
| Design | **Screen Object Model** + a documented **NameMapping** (keyed on `WinFormsControlName`) |
| Style | **Gherkin/BDD** — `Features/*.feature` bound to thin Python step routines |
| Lifecycle | one fresh SUT instance **per scenario** (`Support/Hooks.py`) |
| Reporting | TestComplete log (`/ExportLog`), desktop picture on failure |

> **This repo is not runnable in CI.** TestComplete/TestExecute is licensed
> commercial software needing an interactive Windows desktop. The deliverable is
> the **framework, patterns and documentation**; the SUT compiles with the .NET 8
> SDK, the TestComplete project opens in the tool. Verification here = the SUT
> builds, the Python parses, every Gherkin step resolves to a step routine, and
> the NameMapping doc matches the SUT's control names.

## Golden rules

1. **Strict layering.**
   - A **step** translates one sentence into one screen call + one assertion. No
     `Aliases`, `Sys`, `NameMapping` paths, waits or locators in a step.
   - A **screen object** exposes intent-revealing actions/queries. It never
     asserts and never calls `Log.Error`/`Log.Checkpoint`.
   - `BaseScreen` owns the only Win32 primitives screens may use (`click`,
     `set_text`, `get_text`, `select_combo`, `set_checkbox`, `menu_select`, …).
2. **NameMapping by stable identity.** Every mapped node keys on
   `WinFormsControlName` (windows also on `WndClass`); never on index or
   screen coordinates. The intent lives in
   `TestCompleteProject/ContactManager/NameMapping/NameMapping.md` — keep it in
   sync with the SUT and the screen objects.
3. **Explicit waits only.** `Support/Waits.py` polls with a timeout budget.
   No `Delay(3000)` guesses in screen code; `for_ui_idle()` is the one allowed
   settle after an input event.
4. **Deterministic scenarios.** A fresh app per scenario; each scenario owns its
   data (`Given the following contacts exist:` or explicit `When I add …`).
   Scenarios pass in any order and can be sharded.
5. **Data-driven where behaviour varies** — a `Scenario Outline` with an
   `Examples` table, not copied scenarios. Reuse existing step phrases before
   inventing new ones.
6. **Modal and native dialogs are just screens.** `AboutDialog` (modal WinForms)
   and `ExportDialog` (native `#32770` Save dialog) both extend `BaseScreen`.
7. **Tag every feature's happy path `@smoke`.**

## Layout

```
sut/ContactManager/                     the WinForms SUT (build with dotnet)
TestCompleteProject/
├── ContactManagerSuite.pjs             project suite (open this in TestComplete)
└── ContactManager/
    ├── ContactManager.mds              project item list (units, BDD, events, vars)
    ├── Features/*.feature              Gherkin, one file per area
    ├── NameMapping/NameMapping.md      the mapping's intent (binary .tcNM is tool-made)
    └── Script/
        ├── ScreenObjects/             BaseScreen, MainScreen, AboutDialog, ExportDialog
        ├── StepDefs/                  CommonSteps, ContactSteps, EditSteps, ExportSteps, AboutSteps
        └── Support/                   Config, Waits, Hooks
docs/                                   SOM, BDD integration, distributed execution
.claude/                                agents + skills for the AI-assisted workflow
```

## Definition of done

- `cd sut && dotnet build -c Release` succeeds (add controls with an explicit `Name`).
- Every Gherkin step in `Features/` matches a `@step` pattern in `Script/StepDefs/`.
- New UI surface → a new/updated screen object **and** a NameMapping.md entry.
- New behaviour variation → `Examples` rows, not duplicated scenarios.
- No `Aliases`/`Sys`/`Delay` in a step; no assertion in a screen object.
- `docs/` still describes what the code does.
