# Screen Object Model (SOM)

The desktop equivalent of the web Page Object Model. Each **window or dialog** in
the application is represented by one class that exposes *what a user can do on
that screen*, and hides *how* it is done.

## Layers

```
 Feature files (.feature)          business language
        │
 Step definitions (StepDefs/)      one sentence → one screen call + one assertion
        │
 Screen Objects (ScreenObjects/)   user-level actions & queries for one window
        │
 BaseScreen + Support/             object resolution, explicit waits, primitives
        │
 NameMapping + Aliases             stable identity for every control
        │
 The application under test
```

**Rule of thumb:** a layer may only call the layer directly below it. A step
definition that imports `Aliases` or calls `Sys.Process` is a bug.

## What belongs where

| Concern | Home |
|---|---|
| "Add a contact", "delete the selected contact" | Screen Object method |
| Which control to type into | Screen Object (as a NameMapping id constant) |
| Waiting for a window / control | `BaseScreen` / `Support/Waits.py` |
| Launching & closing the app | `Support/Hooks.py` |
| Assertions | Step definitions (via `Log.Checkpoint` / `Log.Error`) |
| Test data & expected strings | Feature files |

## Anatomy of a Screen Object

```python
class MainScreen(BaseScreen):
    ROOT_ALIAS = "MainForm"          # resolves Aliases.ContactManager.MainForm

    FIRST_NAME = "txtFirstName"       # NameMapping ids, not selectors
    ADD_BUTTON = "btnAdd"

    def add_contact(self, first, last, email):   # intent, not mechanics
        self.set_text(self.FIRST_NAME, first)
        ...
        self.click(self.ADD_BUTTON)
        return self                  # fluent, so steps read top-to-bottom

    def visible_contacts(self):      # queries return plain Python values
        ...
```

* **`ROOT_ALIAS`** keeps the mapping in one place and lets `BaseScreen` resolve
  the window lazily (a re-shown window just works).
* **Control ids are constants**, so a NameMapping rename is a one-line change.
* **Actions return `self`** for fluency; **queries return data** (`list`, `int`,
  `str`) — never a raw TestComplete object, so steps can't leak mechanics.

## Modal and native dialogs

`AboutDialog` (a modal WinForms window) maps under the *process*, not under
`MainForm`, and `wait_shown()` waits for the modal window. `ExportDialog` models
the **native** Windows Save dialog (`WndClass = #32770`) the same way. The same
base class and primitives handle all three — an in-app screen, a modal dialog and
an OS dialog are the same shape.

## Why this scales

New coverage means new *feature files* and, at most, a few new screen methods —
the control-identity layer (`NameMapping`) and the waiting strategy
(`Support/Waits.py`) are written once. This repo's ~126 scenarios across 15
feature files reuse the same ~4 screen objects. Because each scenario is
independent (fresh app, own data), the feature folder partitions cleanly across
runners — see [`DISTRIBUTED-EXECUTION.md`](DISTRIBUTED-EXECUTION.md).
