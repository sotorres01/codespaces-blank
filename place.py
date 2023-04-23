class Place:
    def __init__(self, name: str, ubication: str, type_place: str):
        """
        Constructor of the Place class.

        Args:
            name (str): The name of the place.
            ubication (str): The location of the place.
            type_place (str): The type of place.
        """
        self._name = name
        self._ubication = ubication
        self._type_place = type_place

    @property
    def name(self) -> str:
        """
        Gets the name of the place.

        Returns:
            str: The name of the place.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the name of the place.

        Args:
            value (str): The value of the place name.
        """
        self._name = value

    @property
    def ubication(self) -> str:
        """
        Gets the location of the place.

        Returns:
            str: The location of the place.
        """
        return self._ubication

    @ubication.setter
    def ubication(self, value: str) -> None:
        """
        Sets the location of the place.

        Args:
            value (str): The value of the place location.
        """
        self._ubication = value

    @property
    def type_place(self) -> str:
        """
        Gets the type of place.

        Returns:
            str: The type of place.
        """
        return self._type_place

    @type_place.setter
    def type_place(self, value: str) -> None:
        """
        Sets the type of place.

        Args:
            value (str): The value of the place type.
        """
        self._type_place = value
