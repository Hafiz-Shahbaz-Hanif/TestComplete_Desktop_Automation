<!-- See CONTRIBUTING.md and CLAUDE.md for the full conventions. This project is a
     pattern showcase — it is not runnable in CI (TestComplete is licensed). -->

## What & why

<!-- One or two lines. Link the issue if there is one. -->

## Checklist

- [ ] SUT builds (`dotnet build -c Release`)
- [ ] Every Gherkin step line resolves to exactly one `@step` routine
- [ ] Variations are `Examples` rows; steps stay thin; screen objects don't assert
- [ ] `NameMapping/NameMapping.md` and `ContactManager.mds` updated for new controls / units
- [ ] No guessed `Delay(...)` — explicit waits only

## Notes for the reviewer

<!-- Anything non-obvious: a SUT behaviour relied on, a deliberate deviation, follow-ups. -->
