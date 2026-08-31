# NameMapping — strategy and contents

TestComplete stores NameMapping in a binary `NameMapping.tcNM` that is created
and edited inside the tool. This file documents **what that mapping contains and
why**, so the intent survives in the repository and code review.

## Principles

1. **Map by stable identity, never by index or screen coordinates.**
   Every control in the SUT has an explicit `Name` (`txtFirstName`, `btnAdd`, …).
   Each mapped node keys on `WinFormsControlName` (plus `WndClass` for the window).
2. **One alias per control, named for its role, not its widget type.**
   `Aliases.ContactManager.MainForm.txtFirstName` — the alias tree mirrors the
   Screen Object tree.
3. **Windows are mapped as children of the process**; child controls as children
   of their window. Modal dialogs (`AboutForm`) map as a sibling of `MainForm`
   under the process, so they resolve whether or not `MainForm` has focus.
4. **No `Extended Find` bloat** — one hop from parent to child wherever the
   control tree allows it.

## Mapped tree

```
Sys
└── Process("ContactManager")                     → Aliases.ContactManager
    ├── WinFormsObject("MainForm")                → Aliases.ContactManager.MainForm
    │   ├── WinFormsObject("txtFirstName")        → .txtFirstName
    │   ├── WinFormsObject("txtLastName")         → .txtLastName
    │   ├── WinFormsObject("txtEmail")            → .txtEmail
    │   ├── WinFormsObject("btnAdd")              → .btnAdd
    │   ├── WinFormsObject("txtSearch")           → .txtSearch
    │   ├── WinFormsObject("lstContacts")         → .lstContacts
    │   ├── WinFormsObject("btnDelete")           → .btnDelete
    │   ├── WinFormsObject("lblCount")            → .lblCount
    │   ├── WinFormsObject("menuStrip")           → .MainMenu
    │   └── WinFormsObject("statusStrip")         → .statusStrip
    └── WinFormsObject("AboutForm")               → Aliases.ContactManager.AboutForm
        ├── WinFormsObject("lblAbout")            → .lblAbout
        └── WinFormsObject("btnAboutOk")          → .btnAboutOk
```

## Recreating it

1. Open `ContactManagerSuite.pjs` in TestComplete.
2. Build and run the SUT (`../../sut`).
3. Use **Map Object** on each control listed above; set the identification
   property to `WinFormsControlName` and clear any auto-added positional criteria.
4. Rename each alias to match the second column.
