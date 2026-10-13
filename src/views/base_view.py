from abc import ABC, abstractmethod


class BaseView(ABC):
    """Abstract user-facing presentation. Swap the subclass to change the UI."""

    @abstractmethod
    def display_welcome(self) -> None:
        """Banner and greeting."""

    @abstractmethod
    def display_commands(self) -> None:
        """Help page with available commands."""

    @abstractmethod
    def display_contact(self, record) -> None:
        """One contact card."""

    @abstractmethod
    def display_contacts(self, records) -> None:
        """List of contact cards."""

    @abstractmethod
    def display_birthdays(self, birthdays) -> None:
        """Upcoming birthdays."""

    @abstractmethod
    def display_message(self, message: str) -> None:
        """Plain status message."""

    @abstractmethod
    def display_error(self, message: str) -> None:
        """Error message."""

    @abstractmethod
    def prompt(self, text: str) -> str:
        """Read the next user command."""
