---
name: new-feature-coverage
description: Add a Gherkin feature file (plus any screen methods and step routines it needs) covering a Contact Manager capability in this TestComplete SOM/BDD project, data-driven where the behaviour varies.
---

# Add coverage for a capability

## 1. Understand the capability

Read the SUT handler in `sut/ContactManager/MainForm.cs` (and `ContactRepository.cs`)
for the exact behaviour: control names, status-bar wording, validation order,
list rendering (`Contact.ToString()`).

## 2. Reuse the vocabulary first

Grep `Script/StepDefs/` for an existing `@step` that already says what you need.
The common phrases:

- `Given the following contacts exist:` (table: First|Last|Email|Phone|Category|Favourite)
- `When I add a contact "F" "L" with email "E"` / `... and phone "P"`
- `When I search for "…"` · `When I filter by the "X" category` · `When I sort by "X"`
- `When I select the contact "<display text>"` · `When I edit the selected contact`
- `Then the contact count is N` · `the contact list contains "…"` ·
  `the status message contains "…"` · `the count label shows "…"`

Only add a step routine when no phrase fits — keep it thin (one screen call +
one assertion) and put it in the matching `*Steps.py`.

## 3. Write the feature

- `Features/<Area>.feature`, `Background` = `Given the Contact Manager is running`
  (+ `And the contact list is empty` unless the scenario seeds data).
- Tag one happy path `@smoke`.
- Variations → one `Scenario Outline` with an `Examples` table. Make each row's
  expectation exact (compute it from `Contact.ToString()` — favourites get a
  `★ ` prefix).

## 4. Wire and verify

- New step unit → register it in `ContactManager/ContactManager.mds`
  (`<Script>` + `<BDD><StepDefinitionUnits>`).
- New control → screen object + `NameMapping/NameMapping.md` entry.
- ```bash
  cd sut && dotnet build -c Release      # SUT still compiles
  ```
- Walk every new step line and confirm it matches a `@step` pattern.

## Checklist

- [ ] Every step resolves to a routine; new routines are thin
- [ ] Variations are `Examples` rows, not copied scenarios
- [ ] Expected list rows match `Contact.ToString()` exactly
- [ ] `@smoke` on the happy path; `.mds` updated if a unit was added
- [ ] SUT builds
