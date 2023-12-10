"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

from typing import List
from src.leadlistener.data.input.InputFile import InputFile
import datetime


class AudioFile(InputFile):
    """AudioFile Class.

    Represents the audio input file.
    """

    def __init__(self) -> None:
        """Initializes a new instance of AudioFile with default values."""
        super().__init__()
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
    def timestamp(self) -> datetime.time:
        """Getter for the timestamp.

        Returns:
            datetime.time: The timestamp.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self) -> None:
        """Setter for the timestamp.
        """
        self._timestamp = datetime.datetime.now()

    @property
    def id(self) -> str:
        """Getter for the id.

        Returns:
            str: The id.
        """
        return self._id

    def __str__(self) -> str:
        """Return the string representation of the object.

        Provides a human-readable string describing it.

        Returns:
            str: String representation of it.
        """
        return "{} {} {}".format("The Audio Input File path:", self._path, self._timestamp)

    def __eq__(self, value: object) -> bool:
        """Check the equality of this with another object.

        Two are considered equal if they have the same attributes

        Args:
            value (object): The object to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        if isinstance(value, AudioFile):
            return (self._id == value.id and
                    self._path == value.path
                    and self._timestamp == value.timestamp)
        else:
            return False
