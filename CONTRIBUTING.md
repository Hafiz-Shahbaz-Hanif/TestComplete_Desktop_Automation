# Contributing

Thanks for looking at this project. It is a **pattern and architecture showcase**
(see the disclaimer in the README) — it is not runnable in CI because
TestComplete/TestExecute is licensed commercial software. Contributions to the
SUT, the documented framework, or the docs are still welcome.

## Ground rules

The conventions in [`CLAUDE.md`](CLAUDE.md) are the contract — read it first. In
short:

- **Strict layering.** A step = one screen call + one assertion (no `Aliases`,
  `Sys`, waits or locators). A screen object exposes intent, never asserts.
  `BaseScreen` owns the only Win32 primitives.
- **NameMapping by stable identity** — keyed on `WinFormsControlName` (windows
  also on `WndClass`); never by index or coordinates. Keep
  `NameMapping/NameMapping.md` in sync with the SUT.
- **Explicit waits only** (`Support/Waits.py`); no `Delay(3000)` guesses.
- **Deterministic scenarios** — fresh app per scenario, each owns its data.
- **Data-driven** — a `Scenario Outline` with an `Examples` table, not copied
  scenarios.

## What you can verify without TestComplete

```bash
cd sut && dotnet build -c Release          # the SUT compiles (needs .NET 8 SDK)
```

- Every Gherkin step in `Features/` matches a `# @step(r"…")` in `Script/StepDefs/`.
- The NameMapping.md tree matches the SUT's control `Name`s.
- Screen objects contain no `Log.*` / `assert`; steps contain no `Aliases` / `Sys`.

## Adding coverage

1. New capability → read the SUT handler in `sut/ContactManager/` for the exact
   behaviour (control names, status wording, validation order,
   `Contact.ToString()`).
2. Reuse existing step phrases first (`grep Script/StepDefs/`). New step routines
   stay thin and go in the matching `*Steps.py`.
3. New control → a screen object + a `NameMapping/NameMapping.md` entry; register
   any new unit in `ContactManager/ContactManager.mds`.
4. Add the feature file under `Features/`; tag one happy path `@smoke`.

## Before you open a PR

- [ ] SUT builds (`dotnet build -c Release`)
- [ ] Every step line resolves to exactly one routine
- [ ] Variations are `Examples` rows; steps stay thin; screens don't assert
- [ ] `NameMapping.md` and `ContactManager.mds` updated for new controls/units
- [ ] Commit messages are conventional (`feat(sut): …`, `test(bdd): …`, `docs: …`)

## AI-assisted workflow

`.claude/` contains the subagents and skills used to develop this repo
(`screen-object-author`, `namemapping-reviewer`, `scenario-triager`, and the
`new-feature-coverage` / `bdd-step-audit` skills). They encode the same rules as
this document.
