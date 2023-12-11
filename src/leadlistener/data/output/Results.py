"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

from typing import List
import datetime
from src.leadlistener.data.output.Result import Result


class Results():
    """Results Class.

    Represents the results.
    """

    def __init__(self) -> None:
        """Initializes a new instance of Result with default values."""
        super().__init__()
        self._results: List[Result] = []
        self._audio_file = None
        self._location_file = None
        self._id = id(self)
        self._timestamp = None

    @property
    def results(self) -> List[Result]:
        """Getter for the results.

        Returns:
            List[Result]: The results.
        """
        return self._results

    @results.setter
    def results(self, value: List[Result]) -> None:
        """Setter for the results.

        Args:
            value (List[Result]): The results to set.
        """
        self._results = value

    def add_result(self, result: Result) -> None:
        """Add a result to the results.

        Args:
            result (Result): The result to add.
        """
        self._results.append(result)

    def remove_result(self, result: Result) -> None:
        """Remove a result from the results.

        Args:
            result (Result): The result to remove.
        """
        self._results.remove(result)

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
    def audio_file(self) -> str:
        """Getter for the audio file.

        Returns:
            str: The audio file.
        """
        return self._audio_file

    @audio_file.setter
    def audio_file(self, value: str) -> None:
        """Setter for the audio file.

        Args:
            value (str): The audio file to set.
        """
        self._audio_file = value

    @property
    def location_file(self) -> str:
        """Getter for the location file.

        Returns:
            str: The location file.
        """
        return self._location_file

    @location_file.setter
    def location_file(self, value: str) -> None:
        """Setter for the location file.

        Args:
            value (str): The location file to set.
        """
        self._location_file = value

    @property
    def id(self) -> str:
        """Getter for the id.

        Returns:
            str: The id.
        """
        return self._id

    def __eq__(self, value: object) -> bool:
        """Check the equality of this with another object.

        Two are considered equal if they have the same attributes

        Args:
            value (object): The object to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        if isinstance(value, Results):
            return (self._id == value._id and
                self._timestamp == value._timestamp and
                self._audio_file == value._audio_file and
                self._location_file == value._location_file and
                self._results == value._results)
        else:
            return False
