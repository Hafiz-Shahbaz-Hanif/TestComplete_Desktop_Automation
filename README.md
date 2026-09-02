# TestComplete Desktop Automation — Screen Object Model + BDD

![TestComplete](https://img.shields.io/badge/TestComplete-15%2B-2FA84F)
![Language](https://img.shields.io/badge/scripting-Python-3776AB?logo=python&logoColor=white)
![Pattern](https://img.shields.io/badge/pattern-Screen%20Object%20Model-blue)
![BDD](https://img.shields.io/badge/BDD-Gherkin-23D96C?logo=cucumber&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)

A reference implementation of a **Windows desktop** automation framework in
**SmartBear TestComplete**, using **Python scripting**, a **Screen Object Model**
and **Gherkin/BDD**, driving a small open-source **WinForms** application —
**~126 scenarios** across 15 feature files.

> ### Disclaimer
> This repository is a **pattern and architecture showcase**. All code here is
> original and written for this demo. It contains **no proprietary or
> employer code, data, NameMapping, or reports**. TestComplete / TestExecute are
> licensed commercial products from SmartBear and are not included.

---

## What's in here

| Path | Contents |
|---|---|
| `sut/` | **Contact Manager** — a small .NET 8 WinForms app that is the automation target: add / edit / delete contacts, phone + category + favourite fields, validation, search / category / favourite filters, sort, CSV export, About dialog. Build with `dotnet build`. |
| `TestCompleteProject/` | The TestComplete project: Python screen objects, step definitions, support code, 15 Gherkin feature files, and a documented NameMapping. |
| `CLAUDE.md` + `.claude/` | The working agreement, subagents and skills for the **AI-assisted workflow** (screen-object authoring, NameMapping review, scenario triage, BDD audits). |
| `docs/SCREEN-OBJECT-MODEL.md` | The layered SOM design and the rules that keep it maintainable. |
| `docs/DISTRIBUTED-EXECUTION.md` | How an overnight desktop suite went from **72+ h to 2–3 h** by partitioning modules across runners. |
| `docs/BDD-INTEGRATION.md` | How Gherkin steps bind to Python routines and screen objects. |

## The framework at a glance

```
Features/*.feature            →  15 files: add / edit / delete / search / filter / sort /
                                 export / validation / status / about — in business language
Script/StepDefs/*.py          →  one routine per step: one screen call + one assertion
Script/ScreenObjects/*.py     →  MainScreen, AboutDialog, ExportDialog  (extend BaseScreen)
Script/Support/*.py           →  Config, Waits (explicit, no fixed delays), Hooks
NameMapping/                  →  every control keyed on its WinForms control name
```

Design highlights:

- **Strict layering** — a step never touches `Aliases` or `Sys`; a screen never
  asserts. See `docs/SCREEN-OBJECT-MODEL.md`.
- **Explicit waits only** — `Support/Waits.py` polls with a timeout budget;
  there are no `Delay(3000)` guesses in screen code.
- **Deterministic scenarios** — a fresh app instance per scenario (hooks), each
  scenario owns its data, so scenarios run in any order and can be sharded.
- **Data-driven** — behaviour that varies is a `Scenario Outline` with an
  `Examples` table (categories, validation rules, search terms, sort orders).
- **Modal and native dialogs are just screens** — `AboutDialog` (modal WinForms)
  and `ExportDialog` (native `#32770` Save dialog) both extend `BaseScreen`.

## Running it

You need TestComplete 15+ (Desktop + Python modules; a trial works) on Windows.
Full setup steps are in [`TestCompleteProject/project-notes.md`](TestCompleteProject/project-notes.md).

```bash
cd sut && dotnet build -c Release      # build the SUT
# then open TestCompleteProject/ContactManagerSuite.pjs in TestComplete
```

For frameworks you can clone and run in CI today, see the portfolio's
**Playwright**, **Selenium** and **Cypress** repositories.

---

## Author

**Hafiz Shahbaz Hanif** — Staff SQA Engineer / Test Automation Architect
[LinkedIn](https://www.linkedin.com/in/hafiz-shahbaz-hanif-70407417a) · [GitHub](https://github.com/Hafiz-Shahbaz-Hanif)

Licensed under the [MIT License](LICENSE).
