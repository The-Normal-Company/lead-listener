"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

from abc import abstractmethod
import datetime


class InputFile():
    """InputFile Base Class."""

    def __init__(self) -> None:
        """Initializes a new instance of InputFile with default values."""
        self._path: str = ""
        self._id = id(self)
        self._timestamp = None

    @property
    def path(self) -> str:
        """Getter for the path.

        Returns:
            str: The path of the file.
        """
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        """Setter for the path of the input.

        Args:
            value (str): The path to set for the path.
        """
        self._path = value

    @property
    @abstractmethod
    def timestamp(self) -> datetime.time:
        """Abstract property for timestamp.

        Returns:
            datetime.time: Timestamp for datetime.
        """
        raise NotImplementedError

    @timestamp.setter
    @abstractmethod
    def timestamp(self) -> datetime.datetime:
        """Abstract setter for timestamp.
        """
        raise NotImplementedError

    @property
    def id(self) -> str:
        """Getter for the path.

        Returns:
            str: The id.
        """
        return self._id
