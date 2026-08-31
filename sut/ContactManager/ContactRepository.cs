namespace ContactManager;

/// <summary>In-memory contact store. Kept deliberately simple - this app exists
/// only as a stable target for the TestComplete automation showcase.</summary>
public sealed class ContactRepository
{
    private readonly List<Contact> _contacts = new();

    public IReadOnlyList<Contact> All => _contacts;

    public bool Add(Contact contact)
    {
        if (_contacts.Any(c => c.Email.Equals(contact.Email, StringComparison.OrdinalIgnoreCase)))
        {
            return false;
        }

        _contacts.Add(contact);
        return true;
    }

    public bool Remove(Contact contact) => _contacts.Remove(contact);

    public IEnumerable<Contact> Search(string term)
    {
        if (string.IsNullOrWhiteSpace(term))
        {
            return _contacts;
        }

        return _contacts.Where(c =>
            c.FullName.Contains(term, StringComparison.OrdinalIgnoreCase) ||
            c.Email.Contains(term, StringComparison.OrdinalIgnoreCase));
    }
}
