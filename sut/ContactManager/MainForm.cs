using System.Text.RegularExpressions;

namespace ContactManager;

public partial class MainForm : Form
{
    private static readonly Regex EmailPattern =
        new(@"^[^@\s]+@[^@\s]+\.[^@\s]+$", RegexOptions.Compiled);

    private readonly ContactRepository _repository = new();

    public MainForm()
    {
        InitializeComponent();
        RefreshList();
    }

    private void OnAddClicked(object? sender, EventArgs e)
    {
        var first = txtFirstName.Text.Trim();
        var last = txtLastName.Text.Trim();
        var email = txtEmail.Text.Trim();

        if (first.Length == 0 || last.Length == 0)
        {
            SetStatus("First and last name are required.");
            return;
        }

        if (!EmailPattern.IsMatch(email))
        {
            SetStatus("Please enter a valid email address.");
            return;
        }

        if (!_repository.Add(new Contact(first, last, email)))
        {
            SetStatus($"A contact with email {email} already exists.");
            return;
        }

        txtFirstName.Clear();
        txtLastName.Clear();
        txtEmail.Clear();
        RefreshList();
        SetStatus($"Added {first} {last}.");
    }

    private void OnDeleteClicked(object? sender, EventArgs e)
    {
        if (lstContacts.SelectedItem is not Contact selected)
        {
            SetStatus("Select a contact to delete.");
            return;
        }

        _repository.Remove(selected);
        RefreshList();
        SetStatus($"Deleted {selected.FullName}.");
    }

    private void OnSearchChanged(object? sender, EventArgs e) => RefreshList();

    private void OnExitClicked(object? sender, EventArgs e) => Close();

    private void OnAboutClicked(object? sender, EventArgs e)
    {
        using var about = new AboutForm();
        about.ShowDialog(this);
    }

    private void RefreshList()
    {
        var matches = _repository.Search(txtSearch.Text.Trim()).ToArray();
        lstContacts.BeginUpdate();
        lstContacts.Items.Clear();
        lstContacts.Items.AddRange(matches.Cast<object>().ToArray());
        lstContacts.EndUpdate();
        lblCount.Text = $"{matches.Length} contact(s)";
    }

    private void SetStatus(string message) => lblStatus.Text = message;
}
