using System.Text;

namespace ContactManager;

public enum SortKey
{
    Name,
    Email,
    Category,
}

/// <summary>In-memory contact store. Kept deliberately simple - this app exists
/// only as a stable target for the TestComplete automation showcase.</summary>
public sealed class ContactRepository
{
    private readonly List<Contact> _contacts = new();

    public IReadOnlyList<Contact> All => _contacts;

    public bool Add(Contact contact)
    {
        if (Exists(contact.Email))
        {
            return false;
        }

        _contacts.Add(contact);
        return true;
    }

    /// <summary>Replace the contact identified by <paramref name="originalEmail"/>.
    /// Returns false if the new email collides with a different contact.</summary>
    public bool Update(string originalEmail, Contact updated)
    {
        var index = _contacts.FindIndex(c => SameEmail(c.Email, originalEmail));
        if (index < 0)
        {
            return false;
        }

        var clash = _contacts.Any(c =>
            !SameEmail(c.Email, originalEmail) && SameEmail(c.Email, updated.Email));
        if (clash)
        {
            return false;
        }

        _contacts[index] = updated;
        return true;
    }

    public bool Remove(Contact contact) => _contacts.Remove(contact);

    public bool Exists(string email) => _contacts.Any(c => SameEmail(c.Email, email));

    public void Clear() => _contacts.Clear();

    public IEnumerable<Contact> Query(string term, ContactCategory? category, bool favouritesOnly)
    {
        IEnumerable<Contact> result = _contacts;

        if (!string.IsNullOrWhiteSpace(term))
        {
            result = result.Where(c =>
                c.FullName.Contains(term, StringComparison.OrdinalIgnoreCase) ||
                c.Email.Contains(term, StringComparison.OrdinalIgnoreCase) ||
                c.Phone.Contains(term, StringComparison.OrdinalIgnoreCase));
        }

        if (category is { } wanted)
        {
            result = result.Where(c => c.Category == wanted);
        }

        if (favouritesOnly)
        {
            result = result.Where(c => c.IsFavourite);
        }

        return result;
    }

    public static IEnumerable<Contact> Sort(IEnumerable<Contact> contacts, SortKey key) => key switch
    {
        SortKey.Email => contacts.OrderBy(c => c.Email, StringComparer.OrdinalIgnoreCase),
        SortKey.Category => contacts
            .OrderBy(c => c.Category.ToString(), StringComparer.OrdinalIgnoreCase)
            .ThenBy(c => c.FullName, StringComparer.OrdinalIgnoreCase),
        _ => contacts.OrderBy(c => c.FullName, StringComparer.OrdinalIgnoreCase),
    };

    public void ExportCsv(string path)
    {
        var sb = new StringBuilder();
        sb.AppendLine("FirstName,LastName,Email,Phone,Category,Favourite");
        foreach (var c in _contacts)
        {
            sb.AppendLine($"{Escape(c.FirstName)},{Escape(c.LastName)},{Escape(c.Email)}," +
                          $"{Escape(c.Phone)},{c.Category},{c.IsFavourite}");
        }

        File.WriteAllText(path, sb.ToString());
    }

    private static bool SameEmail(string a, string b) =>
        a.Equals(b, StringComparison.OrdinalIgnoreCase);

    private static string Escape(string value) =>
        value.Contains(',') || value.Contains('"')
            ? $"\"{value.Replace("\"", "\"\"")}\""
            : value;
}
