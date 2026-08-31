# BDD integration

How Gherkin feature files drive the Python screen objects in TestComplete.

## Moving parts

| Piece | Location | Role |
|---|---|---|
| Feature files | `TestCompleteProject/ContactManager/Features/*.feature` | behaviour in business language |
| Step definitions | `Script/StepDefs/*.py` | one routine per step line |
| Screen objects | `Script/ScreenObjects/*.py` | the actions each step performs |
| Hooks | `Script/Support/Hooks.py` | fresh app per scenario, screenshot on failure |

## How a step line binds to a routine

TestComplete's BDD plugin matches a step's text to a step-definition routine.
In this project every step routine carries a `# @step(r"...")` comment holding
the regular expression it satisfies, e.g.

```gherkin
When I add a contact "Hafiz" "Hanif" with email "hafiz@example.com"
```

```python
# @step(r"I add a contact \"(.+)\" \"(.+)\" with email \"(.+)\"")
def add_contact(first_name, last_name, email):
    MainScreen().add_contact(first_name, last_name, email)
```

The capture groups become the routine's positional arguments, in order. Keeping
the pattern next to the code means a reviewer can verify the binding without
opening TestComplete.

## Keeping steps thin

A step definition does exactly two things:

1. translate the sentence into **one** screen-object call, and
2. record **one** assertion via `Log.Checkpoint` (pass) or `Log.Error` (fail).

No waits, no `Sys`, no NameMapping paths, no branching. If a step needs more than
that, the missing behaviour belongs in a screen object.

## Lifecycle

```
Feature
 └─ Scenario
     ├─ on_scenario_start(scenario)   → launch SUT, wait for MainForm
     ├─ Background steps
     ├─ Scenario steps
     └─ on_scenario_end(scenario)     → screenshot if failed, close SUT
```

Every scenario starts from an empty application, so scenarios are independent and
can run in any order (a prerequisite for the distributed execution model in
`DISTRIBUTED-EXECUTION.md`).

## Tags

`@smoke` marks the thin happy-path set. Run only those from TestExecute with
`/tags:@smoke`, or from the TestComplete UI via the feature filter.
