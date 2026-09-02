namespace ContactManager;

public enum ContactCategory
{
    Other,
    Family,
    Friends,
    Work,
}

public sealed record Contact(
    string FirstName,
    string LastName,
    string Email,
    string Phone = "",
    ContactCategory Category = ContactCategory.Other,
    bool IsFavourite = false)
{
    public string FullName => $"{FirstName} {LastName}".Trim();

    /// <summary>The exact text a mapped ListBox row renders - the automation asserts on this.</summary>
    public override string ToString()
    {
        var star = IsFavourite ? "★ " : "";
        return $"{star}{FullName} <{Email}>";
    }
}
