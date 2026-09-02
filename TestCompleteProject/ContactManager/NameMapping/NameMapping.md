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
   of their window. Modal dialogs (`AboutForm`, and the native `Export contacts`
   Save dialog) map as siblings of `MainForm` under the process, so they resolve
   whether or not `MainForm` has focus.
4. **No `Extended Find` bloat** — one hop from parent to child wherever the
   control tree allows it. `menuStrip` is mapped once as `MainMenu`; individual
   items are driven by caption path (`File|Export to CSV...`), not mapped nodes.
5. **The native Save dialog is mapped by window class**, not by title, so a
   localised Windows still resolves it.

## Mapped tree

```
Sys
└── Process("ContactManager")                     → Aliases.ContactManager
    ├── WinFormsObject("MainForm")                → Aliases.ContactManager.MainForm
    │   ├── WinFormsObject("txtFirstName")        → .txtFirstName
    │   ├── WinFormsObject("txtLastName")         → .txtLastName
    │   ├── WinFormsObject("txtEmail")            → .txtEmail
    │   ├── WinFormsObject("txtPhone")            → .txtPhone
    │   ├── WinFormsObject("cboCategory")         → .cboCategory
    │   ├── WinFormsObject("chkFavourite")        → .chkFavourite
    │   ├── WinFormsObject("btnAdd")              → .btnAdd
    │   ├── WinFormsObject("btnSave")             → .btnSave
    │   ├── WinFormsObject("btnEdit")             → .btnEdit
    │   ├── WinFormsObject("btnClear")            → .btnClear
    │   ├── WinFormsObject("txtSearch")           → .txtSearch
    │   ├── WinFormsObject("cboFilterCategory")   → .cboFilterCategory
    │   ├── WinFormsObject("chkFavouritesOnly")   → .chkFavouritesOnly
    │   ├── WinFormsObject("cboSort")             → .cboSort
    │   ├── WinFormsObject("lstContacts")         → .lstContacts
    │   ├── WinFormsObject("btnDelete")           → .btnDelete
    │   ├── WinFormsObject("lblCount")            → .lblCount
    │   ├── WinFormsObject("menuStrip")           → .MainMenu
    │   └── WinFormsObject("statusStrip")         → .statusStrip
    ├── WinFormsObject("AboutForm")               → Aliases.ContactManager.AboutForm
    │   ├── WinFormsObject("lblVersion")          → .lblVersion
    │   ├── WinFormsObject("lblAbout")            → .lblAbout
    │   └── WinFormsObject("btnAboutOk")          → .btnAboutOk
    └── Window("#32770", "Export contacts")       → Aliases.ContactManager.ExportDialog
        ├── Window("Edit", "*", 1)                → .FileName
        └── Window("Button", "Save", 1)           → .SaveButton
```

## Recreating it

1. Open `ContactManagerSuite.pjs` in TestComplete.
2. Build and run the SUT (`../../sut`).
3. Use **Map Object** on each control listed above; set the identification
   property to `WinFormsControlName` and clear any auto-added positional criteria.
4. For the native `Export contacts` dialog, map the window by `WndClass = #32770`
   and the two children by class + caption.
5. Rename each alias to match the second column.
