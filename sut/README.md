# Contact Manager — System Under Test

A deliberately small .NET 8 **WinForms** application that exists purely as a **stable,
open target** for the TestComplete automation showcase in the parent repository.

## Build & run

```bash
cd sut
dotnet build -c Release
dotnet run --project ContactManager       # or run bin/Release/net8.0-windows/ContactManager.exe
```

Requires the **.NET 8 SDK** on Windows (`winget install Microsoft.DotNet.SDK.8`).

## What it does

| Feature | Controls |
|---|---|
| Add a contact — name, email, phone, category, favourite | `txtFirstName`, `txtLastName`, `txtEmail`, `txtPhone`, `cboCategory`, `chkFavourite`, `btnAdd` |
| Edit the selected contact and save changes | `btnEdit` / `mnuEditEdit`, `btnSave` |
| Clear the entry form | `btnClear` |
| Field validation — required name, email format, phone format, duplicate email | `lblStatus` shows the reason |
| Filter as you type, by category, and by favourite | `txtSearch`, `cboFilterCategory`, `chkFavouritesOnly` |
| Sort by name / email / category | `cboSort` |
| Delete the selected contact | `lstContacts`, `btnDelete` / `mnuEditDelete` |
| Live count (`N contact(s)` / `N of M contact(s)` when filtered) | `lblCount` |
| File ▸ New list (clear all) | `menuStrip` ▸ `mnuFileNew` |
| File ▸ Export to CSV… (native `SaveFileDialog`) | `mnuFileExport` |
| File ▸ Exit | `mnuFileExit` |
| Help ▸ About (modal dialog) | `mnuHelpAbout`, `AboutForm` |

Every control has an explicit, stable `Name`, which is what the TestComplete
**NameMapping** binds to (see `../TestCompleteProject/ContactManager/NameMapping/`).

State is in-memory only; each launch starts empty, which keeps automation runs
deterministic.
