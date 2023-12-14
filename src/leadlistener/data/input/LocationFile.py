"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

from typing import List
from src.leadlistener.data.input.InputFile import InputFile
import datetime
import csv


class LocationFile(InputFile):
    """LocationFile Class.

    Represents the location input file.
    """

    def __init__(self) -> None:
        """Initializes a new instance of LocationFile with default values."""
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

    @property
    def lat(self) -> float:
        """Getter for the latitude.

        Returns:
            float: The latitude.
        """
        return self.read_from_csv(self._path, "lat")

    @property
    def lon(self) -> float:
        """Getter for the longitude.

        Returns:
            float: The longitude.
        """
        return self.read_from_csv(self._path, "lon")

    def __str__(self) -> str:
        """Return the string representation of the object.

        Provides a human-readable string describing it.

        Returns:
            str: String representation of it.
        """
        return "{} {} {}".format("The Location Input File path:", self._path, self._timestamp)

    def __eq__(self, value: object) -> bool:
        """Check the equality of this with another object.

        Two are considered equal if they have the same attributes

        Args:
            value (object): The object to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        if isinstance(value, LocationFile):
            return (self._id == value.id and
                    self._path == value.path
                    and self._timestamp == value.timestamp)
        else:
            return False

    def read_from_csv(self, file_path, column_name):
        """Reads latitude from a specified column in a CSV file.

        Args:
            file_path (str): The path to the CSV file.
            lat_column_name (str): The name of the column containing latitude values.

        Returns:
            float: The latitude value from the first row, or None if not found.
        """
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lat = row[column_name]
                return float(lat)
