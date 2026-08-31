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
        ClientSize = new Size(300, 120);

        var message = new Label
        {
            Name = "lblAbout",
            Text = "Contact Manager 1.0\nSample app for the TestComplete automation showcase.",
            Location = new Point(16, 16),
            AutoSize = true,
        };

        var ok = new Button
        {
            Name = "btnAboutOk",
            Text = "OK",
            DialogResult = DialogResult.OK,
            Location = new Point(110, 78),
            Width = 80,
        };

        Controls.Add(message);
        Controls.Add(ok);
        AcceptButton = ok;
    }
}
