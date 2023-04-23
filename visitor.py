from person import Person
from autorizedPersonnel import AutorizedPersonnel
from event import Event

class Visitor(Person):
    """A class representing a visitor attending an event."""

    def __init__(self, responsible: AutorizedPersonnel, event: Event, name: str = 'name', email: str = 'email', telephone: str = 'telephone', id: int = 0):
        """
        Constructs a new Visitor object.

        Args:
            responsible (AutorizedPersonnel): The authorized personnel responsible for the visitor.
            event (Event): The event that the visitor is attending.
            name (str, optional): The name of the visitor. Defaults to 'name'.
            email (str, optional): The email of the visitor. Defaults to 'email'.
            telephone (str, optional): The telephone number of the visitor. Defaults to 'telephone'.
            id (int, optional): The ID of the visitor. Defaults to 0.
        """
        super().__init__(name, email, telephone, id)
        self.responsible = responsible
        self.event = event

    @property
    def responsible(self) -> AutorizedPersonnel:
        """Getter for the authorized personnel responsible for the visitor."""
        return self._responsible

    @responsible.setter
    def responsible(self, value) -> None:
        """Setter for the authorized personnel responsible for the visitor."""
        self._responsible = value

    @property
    def event(self) -> Event:
        """Getter for the event that the visitor is attending."""
        return self._event

    @event.setter
    def event(self, value) -> None:
        """Setter for the event that the visitor is attending."""
        self._event = value

    def __str__(self) -> str:
        """Returns a string representation of the Visitor object."""
        return f"Visitor: {self.responsible} - {self.event} - {self.name} - {self.email} - {self.telephone} - {self.id}"

    def __eq__(self, other) -> bool:
        """
        Determines whether two Visitor objects are equal.

        Args:
            other (Visitor): The other Visitor object to compare.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if isinstance(other, Visitor):
            return super().__eq__(other) and self.responsible == other.responsible and self.event == other.event
        return False
