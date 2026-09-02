namespace ContactManager;

partial class MainForm
{
    private System.ComponentModel.IContainer components = null;

    private MenuStrip menuStrip;
    private ToolStripMenuItem mnuFile;
    private ToolStripMenuItem mnuFileNew;
    private ToolStripMenuItem mnuFileExport;
    private ToolStripMenuItem mnuFileExit;
    private ToolStripMenuItem mnuEdit;
    private ToolStripMenuItem mnuEditEdit;
    private ToolStripMenuItem mnuEditDelete;
    private ToolStripMenuItem mnuHelp;
    private ToolStripMenuItem mnuHelpAbout;

    private Label lblFirstName;
    private TextBox txtFirstName;
    private Label lblLastName;
    private TextBox txtLastName;
    private Label lblEmail;
    private TextBox txtEmail;
    private Label lblPhone;
    private TextBox txtPhone;
    private Label lblCategory;
    private ComboBox cboCategory;
    private CheckBox chkFavourite;

    private Button btnAdd;
    private Button btnEdit;
    private Button btnSave;
    private Button btnClear;

    private Label lblSearch;
    private TextBox txtSearch;
    private Label lblFilterCategory;
    private ComboBox cboFilterCategory;
    private CheckBox chkFavouritesOnly;
    private Label lblSort;
    private ComboBox cboSort;

    private ListBox lstContacts;
    private Button btnDelete;
    private Label lblCount;

    private StatusStrip statusStrip;
    private ToolStripStatusLabel lblStatus;

    protected override void Dispose(bool disposing)
    {
        if (disposing && components != null)
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    private void InitializeComponent()
    {
        components = new System.ComponentModel.Container();

        // --- menu -------------------------------------------------------
        menuStrip = new MenuStrip { Name = "menuStrip" };
        mnuFile = new ToolStripMenuItem { Name = "mnuFile", Text = "&File" };
        mnuFileNew = new ToolStripMenuItem { Name = "mnuFileNew", Text = "&New list" };
        mnuFileExport = new ToolStripMenuItem { Name = "mnuFileExport", Text = "&Export to CSV..." };
        mnuFileExit = new ToolStripMenuItem { Name = "mnuFileExit", Text = "E&xit" };
        mnuFile.DropDownItems.Add(mnuFileNew);
        mnuFile.DropDownItems.Add(mnuFileExport);
        mnuFile.DropDownItems.Add(new ToolStripSeparator());
        mnuFile.DropDownItems.Add(mnuFileExit);

        mnuEdit = new ToolStripMenuItem { Name = "mnuEdit", Text = "&Edit" };
        mnuEditEdit = new ToolStripMenuItem { Name = "mnuEditEdit", Text = "&Edit selected" };
        mnuEditDelete = new ToolStripMenuItem { Name = "mnuEditDelete", Text = "&Delete selected" };
        mnuEdit.DropDownItems.Add(mnuEditEdit);
        mnuEdit.DropDownItems.Add(mnuEditDelete);

        mnuHelp = new ToolStripMenuItem { Name = "mnuHelp", Text = "&Help" };
        mnuHelpAbout = new ToolStripMenuItem { Name = "mnuHelpAbout", Text = "&About" };
        mnuHelp.DropDownItems.Add(mnuHelpAbout);

        menuStrip.Items.Add(mnuFile);
        menuStrip.Items.Add(mnuEdit);
        menuStrip.Items.Add(mnuHelp);

        // --- entry form -----------------------------------------------
        lblFirstName = new Label { Name = "lblFirstName", Text = "First name", Location = new Point(16, 40), AutoSize = true };
        txtFirstName = new TextBox { Name = "txtFirstName", Location = new Point(120, 37), Width = 200 };

        lblLastName = new Label { Name = "lblLastName", Text = "Last name", Location = new Point(16, 72), AutoSize = true };
        txtLastName = new TextBox { Name = "txtLastName", Location = new Point(120, 69), Width = 200 };

        lblEmail = new Label { Name = "lblEmail", Text = "Email", Location = new Point(16, 104), AutoSize = true };
        txtEmail = new TextBox { Name = "txtEmail", Location = new Point(120, 101), Width = 200 };

        lblPhone = new Label { Name = "lblPhone", Text = "Phone", Location = new Point(16, 136), AutoSize = true };
        txtPhone = new TextBox { Name = "txtPhone", Location = new Point(120, 133), Width = 200 };

        lblCategory = new Label { Name = "lblCategory", Text = "Category", Location = new Point(16, 168), AutoSize = true };
        cboCategory = new ComboBox
        {
            Name = "cboCategory",
            Location = new Point(120, 165),
            Width = 200,
            DropDownStyle = ComboBoxStyle.DropDownList,
        };
        cboCategory.Items.AddRange(new object[] { "Other", "Family", "Friends", "Work" });
        cboCategory.SelectedIndex = 0;

        chkFavourite = new CheckBox { Name = "chkFavourite", Text = "Favourite", Location = new Point(120, 193), AutoSize = true };

        btnAdd = new Button { Name = "btnAdd", Text = "Add contact", Location = new Point(120, 220), Width = 120 };
        btnAdd.Click += OnAddClicked;

        btnSave = new Button { Name = "btnSave", Text = "Save changes", Location = new Point(246, 220), Width = 120, Enabled = false };
        btnSave.Click += OnSaveClicked;

        btnEdit = new Button { Name = "btnEdit", Text = "Edit selected", Location = new Point(16, 256), Width = 120 };
        btnEdit.Click += OnEditClicked;

        btnClear = new Button { Name = "btnClear", Text = "Clear form", Location = new Point(142, 256), Width = 100 };
        btnClear.Click += OnClearClicked;

        // --- filters --------------------------------------------------
        lblSearch = new Label { Name = "lblSearch", Text = "Search", Location = new Point(16, 300), AutoSize = true };
        txtSearch = new TextBox { Name = "txtSearch", Location = new Point(120, 297), Width = 200 };
        txtSearch.TextChanged += OnFilterChanged;

        lblFilterCategory = new Label { Name = "lblFilterCategory", Text = "In category", Location = new Point(16, 332), AutoSize = true };
        cboFilterCategory = new ComboBox
        {
            Name = "cboFilterCategory",
            Location = new Point(120, 329),
            Width = 200,
            DropDownStyle = ComboBoxStyle.DropDownList,
        };
        cboFilterCategory.Items.AddRange(new object[] { "All", "Other", "Family", "Friends", "Work" });
        cboFilterCategory.SelectedIndex = 0;
        cboFilterCategory.SelectedIndexChanged += OnFilterChanged;

        chkFavouritesOnly = new CheckBox { Name = "chkFavouritesOnly", Text = "Favourites only", Location = new Point(120, 357), AutoSize = true };
        chkFavouritesOnly.CheckedChanged += OnFilterChanged;

        lblSort = new Label { Name = "lblSort", Text = "Sort by", Location = new Point(16, 385), AutoSize = true };
        cboSort = new ComboBox
        {
            Name = "cboSort",
            Location = new Point(120, 382),
            Width = 200,
            DropDownStyle = ComboBoxStyle.DropDownList,
        };
        cboSort.Items.AddRange(new object[] { "Name", "Email", "Category" });
        cboSort.SelectedIndex = 0;
        cboSort.SelectedIndexChanged += OnFilterChanged;

        // --- list ---------------------------------------------------
        lstContacts = new ListBox { Name = "lstContacts", Location = new Point(16, 416), Size = new Size(414, 150) };

        btnDelete = new Button { Name = "btnDelete", Text = "Delete selected", Location = new Point(16, 574), Width = 130 };
        btnDelete.Click += OnDeleteClicked;

        lblCount = new Label { Name = "lblCount", Text = "0 contact(s)", Location = new Point(160, 579), AutoSize = true };

        statusStrip = new StatusStrip { Name = "statusStrip" };
        lblStatus = new ToolStripStatusLabel { Name = "lblStatus", Text = "Ready" };
        statusStrip.Items.Add(lblStatus);

        Controls.AddRange(new Control[]
        {
            lblFirstName, txtFirstName, lblLastName, txtLastName, lblEmail, txtEmail,
            lblPhone, txtPhone, lblCategory, cboCategory, chkFavourite,
            btnAdd, btnSave, btnEdit, btnClear,
            lblSearch, txtSearch, lblFilterCategory, cboFilterCategory,
            chkFavouritesOnly, lblSort, cboSort,
            lstContacts, btnDelete, lblCount,
            statusStrip, menuStrip,
        });

        MainMenuStrip = menuStrip;
        mnuFileNew.Click += OnNewListClicked;
        mnuFileExport.Click += OnExportClicked;
        mnuFileExit.Click += OnExitClicked;
        mnuEditEdit.Click += OnEditClicked;
        mnuEditDelete.Click += OnDeleteClicked;
        mnuHelpAbout.Click += OnAboutClicked;

        AutoScaleMode = AutoScaleMode.Font;
        ClientSize = new Size(446, 630);
        FormBorderStyle = FormBorderStyle.FixedSingle;
        MaximizeBox = false;
        Name = "MainForm";
        Text = "Contact Manager";
    }
}
