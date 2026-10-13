from helper.color_loger import log_error
from views.base_view import BaseView


class ConsoleView(BaseView):
    """Console implementation of the user interface."""

    COMMANDS = (
        ("hello", ""),
        ("add <username> <phone>", ""),
        ("change <username> <old_phone> <new_phone>", ""),
        ("remove_phone <username> <phone>", "remove phone from contact"),
        ("remove <username>", "remove contact"),
        ("phone <username>", ""),
        ("add-birthday <username> <birthday> Format:DD.MM.YYYY", ""),
        ("show-birthday <username>", ""),
        ("birthdays", ""),
        ("all", ""),
        ("close, exit", ""),
    )

    WELCOME_BANNER = """
 █████╗ ███████╗███████╗██╗███████╗████████╗ █████╗ ███╗   ██╗████████╗    ██████╗  ██████╗ ████████╗
██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝    ██╔══██╗██╔═══██╗╚══██╔══╝
███████║███████╗███████╗██║███████╗   ██║   ███████║██╔██╗ ██║   ██║       ██████╔╝██║   ██║   ██║
██╔══██║╚════██║╚════██║██║╚════██║   ██║   ██╔══██║██║╚██╗██║   ██║       ██╔══██╗██║   ██║   ██║
██║  ██║███████║███████║██║███████║   ██║   ██║  ██║██║ ╚████║   ██║       ██████╔╝╚██████╔╝   ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═════╝  ╚═════╝    ╚═╝
"""

    def display_welcome(self) -> None:
        print(self.WELCOME_BANNER)
        print("Welcome to the assistant bot!")

    def display_commands(self) -> None:
        print("  Commands:")
        print("  ---------")
        for index, (usage, description) in enumerate(self.COMMANDS, start=1):
            print(f"  {index}. {usage}")
            if description:
                print(f"    Description: {description}")
        print("  ---------")

    def display_contact(self, record) -> None:
        print(self._format_contact(record))

    def display_contacts(self, records) -> None:
        records = list(records)
        if not records:
            print("No contacts")
            return
        for record in records:
            print(self._format_contact(record))

    def display_birthdays(self, birthdays) -> None:
        if not birthdays:
            print("No upcoming birthdays")
            return
        for birthday in birthdays:
            print(f"Name: {birthday['name']}, Birthday: {birthday['congratulation_date']}")

    def display_message(self, message: str) -> None:
        print(message)

    def display_error(self, message: str) -> None:
        log_error(message)

    def prompt(self, text: str) -> str:
        return input(text)

    def _format_contact(self, record) -> str:
        phones = "; ".join(phone.value for phone in record.phones) or "No phones"
        birthday = record.birthday.value if record.birthday else "No birthday"
        return (
            "-------------------------\n"
            f"Name:     {record.name.value}\n"
            f"Phones:   {phones}\n"
            f"Birthday: {birthday}\n"
            "-------------------------"
        )
