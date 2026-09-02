using System.Text.RegularExpressions;

namespace ContactManager;

public partial class MainForm : Form
{
    private static readonly Regex EmailPattern =
        new(@"^[^@\s]+@[^@\s]+\.[^@\s]+$", RegexOptions.Compiled);

    private static readonly Regex PhonePattern =
        new(@"^[0-9 +().\-]{7,}$", RegexOptions.Compiled);

    private readonly ContactRepository _repository = new();

    /// <summary>Email of the contact currently loaded for editing, or null when adding.</summary>
    private string? _editKey;

    public MainForm()
    {
        InitializeComponent();
        RefreshList();
    }

    private void OnAddClicked(object? sender, EventArgs e)
    {
        if (!TryReadForm(out var contact, out var error))
        {
            SetStatus(error);
            return;
        }

        if (!_repository.Add(contact))
        {
            SetStatus($"A contact with email {contact.Email} already exists.");
            return;
        }

        ClearForm();
        RefreshList();
        SetStatus($"Added {contact.FullName}.");
    }

    private void OnEditClicked(object? sender, EventArgs e)
    {
        if (lstContacts.SelectedItem is not Contact selected)
        {
            SetStatus("Select a contact to edit.");
            return;
        }

        txtFirstName.Text = selected.FirstName;
        txtLastName.Text = selected.LastName;
        txtEmail.Text = selected.Email;
        txtPhone.Text = selected.Phone;
        cboCategory.SelectedItem = selected.Category.ToString();
        chkFavourite.Checked = selected.IsFavourite;

        _editKey = selected.Email;
        btnAdd.Enabled = false;
        btnSave.Enabled = true;
        SetStatus($"Editing {selected.FullName}.");
    }

    private void OnSaveClicked(object? sender, EventArgs e)
    {
        if (_editKey is null)
        {
            SetStatus("No contact is being edited.");
            return;
        }

        if (!TryReadForm(out var updated, out var error))
        {
            SetStatus(error);
            return;
        }

        if (!_repository.Update(_editKey, updated))
        {
            SetStatus($"A contact with email {updated.Email} already exists.");
            return;
        }

        ClearForm();
        RefreshList();
        SetStatus($"Updated {updated.FullName}.");
    }

    private void OnClearClicked(object? sender, EventArgs e)
    {
        ClearForm();
        SetStatus("Form cleared.");
    }

    private void OnDeleteClicked(object? sender, EventArgs e)
    {
        if (lstContacts.SelectedItem is not Contact selected)
        {
            SetStatus("Select a contact to delete.");
            return;
        }

        _repository.Remove(selected);
        if (_editKey is not null && _editKey.Equals(selected.Email, StringComparison.OrdinalIgnoreCase))
        {
            ClearForm();
        }

        RefreshList();
        SetStatus($"Deleted {selected.FullName}.");
    }

    private void OnNewListClicked(object? sender, EventArgs e)
    {
        _repository.Clear();
        ClearForm();
        RefreshList();
        SetStatus("Started a new contact list.");
    }

    private void OnExportClicked(object? sender, EventArgs e)
    {
        using var dialog = new SaveFileDialog
        {
            Title = "Export contacts",
            Filter = "CSV files (*.csv)|*.csv",
            FileName = "contacts.csv",
        };

        if (dialog.ShowDialog(this) != DialogResult.OK)
        {
            SetStatus("Export cancelled.");
            return;
        }

        _repository.ExportCsv(dialog.FileName);
        SetStatus($"Exported {_repository.All.Count} contact(s).");
    }

    private void OnFilterChanged(object? sender, EventArgs e) => RefreshList();

    private void OnExitClicked(object? sender, EventArgs e) => Close();

    private void OnAboutClicked(object? sender, EventArgs e)
    {
        using var about = new AboutForm();
        about.ShowDialog(this);
    }

    private bool TryReadForm(out Contact contact, out string error)
    {
        contact = new Contact("", "", "");
        var first = txtFirstName.Text.Trim();
        var last = txtLastName.Text.Trim();
        var email = txtEmail.Text.Trim();
        var phone = txtPhone.Text.Trim();

        if (first.Length == 0 || last.Length == 0)
        {
            error = "First and last name are required.";
            return false;
        }

        if (!EmailPattern.IsMatch(email))
        {
            error = "Please enter a valid email address.";
            return false;
        }

        if (phone.Length > 0 && !PhonePattern.IsMatch(phone))
        {
            error = "Please enter a valid phone number.";
            return false;
        }

        var category = Enum.TryParse<ContactCategory>(cboCategory.SelectedItem?.ToString(), out var parsed)
            ? parsed
            : ContactCategory.Other;

        contact = new Contact(first, last, email, phone, category, chkFavourite.Checked);
        error = "";
        return true;
    }

    private void ClearForm()
    {
        txtFirstName.Clear();
        txtLastName.Clear();
        txtEmail.Clear();
        txtPhone.Clear();
        cboCategory.SelectedIndex = 0;
        chkFavourite.Checked = false;
        _editKey = null;
        btnAdd.Enabled = true;
        btnSave.Enabled = false;
    }

    private void RefreshList()
    {
        var category = cboFilterCategory.SelectedIndex <= 0
            ? (ContactCategory?)null
            : Enum.Parse<ContactCategory>(cboFilterCategory.SelectedItem!.ToString()!);
        var term = txtSearch.Text.Trim();
        var favouritesOnly = chkFavouritesOnly.Checked;
        var sortKey = Enum.Parse<SortKey>(cboSort.SelectedItem?.ToString() ?? "Name");

        var filtered = _repository.Query(term, category, favouritesOnly);
        var matches = ContactRepository.Sort(filtered, sortKey).ToArray();

        lstContacts.BeginUpdate();
        lstContacts.Items.Clear();
        lstContacts.Items.AddRange(matches.Cast<object>().ToArray());
        lstContacts.EndUpdate();

        var total = _repository.All.Count;
        var filtersActive = term.Length > 0 || category is not null || favouritesOnly;
        lblCount.Text = filtersActive
            ? $"{matches.Length} of {total} contact(s)"
            : $"{total} contact(s)";
    }

    private void SetStatus(string message) => lblStatus.Text = message;
}
