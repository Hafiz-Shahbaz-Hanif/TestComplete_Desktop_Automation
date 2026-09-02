# Working with the TestComplete project

## Opening

1. Install **SmartBear TestComplete 15+** with the **Desktop** and **Python**
   modules (a 30-day trial works).
2. Build the SUT: `cd ../sut && dotnet build -c Release`.
3. Open `ContactManagerSuite.pjs` in TestComplete.

The `.pjs` / `.mds` files here are intentionally small and readable so the project
layout is visible in code review. On first open TestComplete may add internal
identifiers and rewrite them into its own format — commit that result.

## First-run setup inside TestComplete

| Step | Where |
|---|---|
| Confirm the **Tested Application** path points at `sut/.../ContactManager.exe` | Project ▸ TestedApps |
| Create the **NameMapping** per `ContactManager/NameMapping/NameMapping.md` | NameMapping editor |
| Wire the **scenario hooks** (`Hooks.on_scenario_start` / `on_scenario_end`) | Project ▸ Properties ▸ Events |
| Point the **BDD feature folder** at `ContactManager/Features` | Project ▸ Properties ▸ BDD |

## Running

* **All scenarios:** run the project (~126 scenarios / outline examples across 15 feature files).
* **Smoke only:** feature filter `@smoke`, or TestExecute `/tags:@smoke` (one happy path per area).
* **Headless / CI:** `TestExecute.exe "ContactManagerSuite.pjs" /run /exit /ExportLog:log.mht`
  on a Windows agent with an interactive desktop session.
* **Sharded:** partition the `Features/` folder across agents — see
  `../docs/DISTRIBUTED-EXECUTION.md`.

## Feature map

| Feature file | Area |
|---|---|
| `AddContact`, `AddValidation`, `PhoneValidation`, `DuplicateEmail` | creating contacts + field validation |
| `EditContact`, `EditValidation` | editing an existing contact, Save-button state machine |
| `DeleteContact` | delete via button and via the Edit menu |
| `SearchContact`, `FilterByCategory`, `SortContacts`, `CountLabel` | list filtering, sorting and the live count |
| `ExportContacts` | File ▸ Export to CSV through the native Save dialog |
| `NewList`, `StatusMessages`, `About` | File ▸ New, status-bar wording, the modal About dialog |

## Why there is no CI workflow

TestComplete/TestExecute is licensed commercial software and needs a real Windows
desktop session. This repo documents the framework and patterns; the runnable,
CI-covered frameworks in the portfolio are the Playwright, Selenium and Cypress
repositories.
