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
| Add a contact (name + email, with validation) | `txtFirstName`, `txtLastName`, `txtEmail`, `btnAdd` |
| Reject duplicates / invalid email | `lblStatus` shows the reason |
| Filter the list as you type | `txtSearch` |
| Delete the selected contact | `lstContacts`, `btnDelete` |
| Live count | `lblCount` |
| File ▸ Exit | `menuStrip` ▸ `mnuFile` ▸ `mnuFileExit` |

Every control has an explicit, stable `Name`, which is what the TestComplete
**NameMapping** binds to (see `../TestCompleteProject/ContactManager/NameMapping/`).

State is in-memory only; each launch starts empty, which keeps automation runs
deterministic.
