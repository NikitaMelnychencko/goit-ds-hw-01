from services.NotebookServices import AddressBook
from services.DataServices import DataServices
from views import ConsoleView
from controlers.index import (
    add_contact, change_contact, find_contact, remove_phone,
    remove_contact, add_birthday, show_birthday, show_birthdays,
    show_all, exit_program
)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    view = ConsoleView()
    data = DataServices()
    book = AddressBook(data.get_init_data())
    view.display_welcome()
    view.display_commands()

    while True:
        user_input = view.prompt("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except Exception:
            view.display_error("Invalid command.")
            continue

        match (command.lower()):
            case "hello":
                view.display_message("How can I help you?")
            case "add":
                add_contact(book, args, view)
            case "change":
                change_contact(book, args, view)
            case "phone":
                find_contact(book, args, view)
            case "remove_phone":
                remove_phone(book, args, view)
            case "remove":
                remove_contact(book, args, view)
            case "add-birthday":
                add_birthday(book, args, view)
            case "show-birthday":
                show_birthday(book, args, view)
            case "birthdays":
                show_birthdays(book, args, view)
            case "all":
                show_all(book, args, view)
            case "exit" | "close":
                if exit_program(book, data, view):
                    break
            case _:
                view.display_error("Invalid command.")

if __name__ == "__main__":
    main()
