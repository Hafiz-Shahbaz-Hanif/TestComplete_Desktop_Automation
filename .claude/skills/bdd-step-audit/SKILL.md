---
name: bdd-step-audit
description: Audit the step definitions and feature files in this TestComplete BDD project for layering violations, dead or duplicate steps, and unbound Gherkin lines.
---

# Audit the BDD layer

## 1. Every Gherkin line binds

For each line in `Features/*.feature` (ignoring `Feature`/`Scenario`/`Background`/
`Examples`/table rows), find a `# @step(r"…")` in `Script/StepDefs/` whose regex
matches after `<placeholder>` substitution. Report any line with **no** match or
**more than one** match.

## 2. Steps stay thin

Flag a step routine that does any of:

- imports/uses `Aliases`, `Sys`, `Region`, `NameMapping` directly
- calls `Delay(` or sleeps
- contains control-flow beyond a single guard (a step is one screen call + one
  assertion / `Log` line)
- reaches into a screen's private control ids to interact, instead of calling a
  screen method

Fix by moving the logic into the relevant `Script/ScreenObjects/*.py`.

## 3. No dead or duplicate steps

- A `@step` routine that no feature line exercises → remove it or add the coverage.
- Two routines whose patterns overlap → merge, or make one strictly more specific.

## 4. Screen objects stay pure

Grep `Script/ScreenObjects/` for `Log.Error`, `Log.Checkpoint`, `assert` — a
screen must not assert. Move it to the step.

## Output

A table: file:line → issue class → fix. End with a one-line verdict
(`clean` / `N issues`).
