from services.NotebookServices import Record


def validate_args(args, required_count, error_message, view):
    """Checks if there are enough arguments for the command"""
    if len(args) < required_count:
        view.display_error(error_message)
        return False
    return True

def find_contact_safe(book, name):
    """Safely finds contact by name"""
    try:
        return book.find(name)
    except Exception:
        return None

def add_contact(book, args, view):
    is_valid = validate_args(args, 2, "Please provide name and phone number", view)
    if is_valid:
        record = find_contact_safe(book, args[0])
        if record:
            record.add_phone(args[1])
            view.display_contacts(book.data.values())
        else:
            record = Record(args[0])
            # Check if the name is valid and not empty
            if hasattr(record.name, 'value') and record.name.value != "":
                record.add_phone(args[1])
                if len(record.phones) > 0:
                    book.add_record(record)
                    view.display_contacts(book.data.values())

def change_contact(book, args, view):
    if not validate_args(args, 3, "Please provide name, old phone number and new phone number", view):
        return

    record = find_contact_safe(book, args[0])
    if record:
        record.edit_phone(args[1], args[2])
        view.display_contacts(book.data.values())
    else:
        view.display_error("Contact not found")

def find_contact(book, args, view):
    if not validate_args(args, 1, "Please provide name", view):
        return

    record = find_contact_safe(book, args[0])
    if record:
        view.display_contact(record)
    else:
        view.display_error("Contact not found")

def remove_phone(book, args, view):
    if not validate_args(args, 2, "Please provide name and phone number", view):
        return

    record = find_contact_safe(book, args[0])
    if record:
        record.remove_phone(args[1])
        view.display_contacts(book.data.values())
    else:
        view.display_error("Contact not found")

def remove_contact(book, args, view):
    if not validate_args(args, 1, "Please provide name", view):
        return

    record = find_contact_safe(book, args[0])
    if record:
        book.delete(args[0])
        view.display_contacts(book.data.values())
    else:
        view.display_error("Contact not found")

def add_birthday(book, args, view):
    if not validate_args(args, 2, "Please provide name and birthday (DD.MM.YYYY)", view):
        return

    record = find_contact_safe(book, args[0])
    if record:
        record.add_birthday(args[1])
        view.display_contacts(book.data.values())
    else:
        view.display_error("Contact not found")

def show_birthday(book, args, view):
    if not validate_args(args, 1, "Please provide name", view):
        return

    record = find_contact_safe(book, args[0])
    if record:
        view.display_contact(record)
    else:
        view.display_error("Contact not found")

def show_birthdays(book, args, view):
    view.display_birthdays(book.get_upcoming_birthdays())

def show_all(book, args, view):
    view.display_contacts(book.data.values())

def exit_program(book, data, view):
    all_book = book.get_contacts_for_json()
    data.save_data(all_book)
    view.display_message("Goodbye!")
    return True
