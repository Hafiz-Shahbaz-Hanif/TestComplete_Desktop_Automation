namespace ContactManager;

public sealed record Contact(string FirstName, string LastName, string Email)
{
    public string FullName => $"{FirstName} {LastName}".Trim();

    public override string ToString() => $"{FullName} <{Email}>";
}
