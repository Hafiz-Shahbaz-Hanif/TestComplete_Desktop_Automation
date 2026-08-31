namespace ContactManager;

partial class MainForm
{
    private System.ComponentModel.IContainer components = null;

    private MenuStrip menuStrip;
    private ToolStripMenuItem mnuFile;
    private ToolStripMenuItem mnuFileExit;
    private ToolStripMenuItem mnuHelp;
    private ToolStripMenuItem mnuHelpAbout;
    private Label lblFirstName;
    private TextBox txtFirstName;
    private Label lblLastName;
    private TextBox txtLastName;
    private Label lblEmail;
    private TextBox txtEmail;
    private Button btnAdd;
    private Label lblSearch;
    private TextBox txtSearch;
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

        menuStrip = new MenuStrip { Name = "menuStrip" };
        mnuFile = new ToolStripMenuItem { Name = "mnuFile", Text = "&File" };
        mnuFileExit = new ToolStripMenuItem { Name = "mnuFileExit", Text = "E&xit" };
        mnuFile.DropDownItems.Add(mnuFileExit);

        mnuHelp = new ToolStripMenuItem { Name = "mnuHelp", Text = "&Help" };
        mnuHelpAbout = new ToolStripMenuItem { Name = "mnuHelpAbout", Text = "&About" };
        mnuHelp.DropDownItems.Add(mnuHelpAbout);

        menuStrip.Items.Add(mnuFile);
        menuStrip.Items.Add(mnuHelp);

        lblFirstName = new Label { Name = "lblFirstName", Text = "First name", Location = new Point(16, 40), AutoSize = true };
        txtFirstName = new TextBox { Name = "txtFirstName", Location = new Point(110, 37), Width = 180 };

        lblLastName = new Label { Name = "lblLastName", Text = "Last name", Location = new Point(16, 72), AutoSize = true };
        txtLastName = new TextBox { Name = "txtLastName", Location = new Point(110, 69), Width = 180 };

        lblEmail = new Label { Name = "lblEmail", Text = "Email", Location = new Point(16, 104), AutoSize = true };
        txtEmail = new TextBox { Name = "txtEmail", Location = new Point(110, 101), Width = 180 };

        btnAdd = new Button { Name = "btnAdd", Text = "Add contact", Location = new Point(110, 133), Width = 120 };
        btnAdd.Click += OnAddClicked;

        lblSearch = new Label { Name = "lblSearch", Text = "Search", Location = new Point(16, 176), AutoSize = true };
        txtSearch = new TextBox { Name = "txtSearch", Location = new Point(110, 173), Width = 180 };
        txtSearch.TextChanged += OnSearchChanged;

        lstContacts = new ListBox { Name = "lstContacts", Location = new Point(16, 204), Size = new Size(274, 160) };

        btnDelete = new Button { Name = "btnDelete", Text = "Delete selected", Location = new Point(16, 372), Width = 130 };
        btnDelete.Click += OnDeleteClicked;

        lblCount = new Label { Name = "lblCount", Text = "0 contact(s)", Location = new Point(170, 377), AutoSize = true };

        statusStrip = new StatusStrip { Name = "statusStrip" };
        lblStatus = new ToolStripStatusLabel { Name = "lblStatus", Text = "Ready" };
        statusStrip.Items.Add(lblStatus);

        Controls.AddRange(new Control[]
        {
            lblFirstName, txtFirstName, lblLastName, txtLastName, lblEmail, txtEmail,
            btnAdd, lblSearch, txtSearch, lstContacts, btnDelete, lblCount,
            statusStrip, menuStrip
        });

        MainMenuStrip = menuStrip;
        mnuFileExit.Click += OnExitClicked;
        mnuHelpAbout.Click += OnAboutClicked;

        AutoScaleMode = AutoScaleMode.Font;
        ClientSize = new Size(320, 430);
        FormBorderStyle = FormBorderStyle.FixedSingle;
        MaximizeBox = false;
        Name = "MainForm";
        Text = "Contact Manager";
    }
}
