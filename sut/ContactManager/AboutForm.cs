namespace ContactManager;

/// <summary>A trivial modal dialog - it gives the automation showcase a second
/// screen (and a modal-window wait) to demonstrate.</summary>
public sealed class AboutForm : Form
{
    public AboutForm()
    {
        Name = "AboutForm";
        Text = "About Contact Manager";
        FormBorderStyle = FormBorderStyle.FixedDialog;
        StartPosition = FormStartPosition.CenterParent;
        MinimizeBox = false;
        MaximizeBox = false;
        ClientSize = new Size(320, 140);

        var version = new Label
        {
            Name = "lblVersion",
            Text = "Contact Manager 2.0",
            Location = new Point(16, 16),
            AutoSize = true,
        };

        var message = new Label
        {
            Name = "lblAbout",
            Text = "Sample app for the TestComplete automation showcase.\nNo proprietary code.",
            Location = new Point(16, 40),
            AutoSize = true,
        };

        var ok = new Button
        {
            Name = "btnAboutOk",
            Text = "OK",
            DialogResult = DialogResult.OK,
            Location = new Point(120, 96),
            Width = 80,
        };

        Controls.Add(version);
        Controls.Add(message);
        Controls.Add(ok);
        AcceptButton = ok;
    }
}
