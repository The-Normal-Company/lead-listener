"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

from typing import List
import datetime


class Result():
    """Result Class.

    Represents the result.
    """

    def __init__(self) -> None:
        """Initializes a new instance of Result with default values."""
        super().__init__()
        self._lat = 0.0
        self._lon = 0.0
        self._type = ""
        self._confidence = 0.0
        self._depth_m = 0.0
        self._depth_ft = 0.0
        self._diameter_m = 0.0
        self._diameter_ft = 0.0
        self._audio_file = None
        self._location_file = None
        self._files_timestamp = None
        self._id = id(self)
        self._timestamp = None
        self._path = ""

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
    def lat(self) -> float:
        """Getter for the latitude.

        Returns:
            float: The latitude.
        """
        return self._lat

    @lat.setter
    def lat(self, value: float) -> None:
        """Setter for the latitude.

        Args:
            value (float): The latitude to set.
        """
        self._lat = value

    @property
    def lon(self) -> float:
        """Getter for the longitude.

        Returns:
            float: The longitude.
        """
        return self._lon

    @lon.setter
    def lon(self, value: float) -> None:
        """Setter for the longitude.

        Args:
            value (float): The longitude to set.
        """
        self._lon = value

    @property
    def type(self) -> str:
        """Getter for the type.

        Returns:
            str: The type.
        """
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        """Setter for the type.

        Args:
            value (str): The type to set.
        """
        self._type = value

    @property
    def confidence(self) -> float:
        """Getter for the confidence.

        Returns:
            float: The confidence.
        """
        return self._confidence

    @confidence.setter
    def confidence(self, value: float) -> None:
        """Setter for the confidence.

        Args:
            value (float): The confidence to set.
        """
        self._confidence = value

    @property
    def depth_m(self) -> float:
        """Getter for the depth in meters.

        Returns:
            float: The depth in meters.
        """
        return self._depth_m

    @depth_m.setter
    def depth_m(self, value: float) -> None:
        """Setter for the depth in meters.

        Args:
            value (float): The depth in meters to set.
        """
        self._depth_ft = value * 3.28084
        self._depth_m = value

    @property
    def depth_ft(self) -> float:
        """Getter for the depth in feet.

        Returns:
            float: The depth in feet.
        """
        return self._depth_ft

    @depth_ft.setter
    def depth_ft(self, value: float) -> None:
        """Setter for the depth in feet.

        Args:
            value (float): The depth in feet to set.
        """
        self._depth_m = value / 3.28084
        self._depth_ft = value

    @property
    def diameter_m(self) -> float:
        """Getter for the diameter in meters.

        Returns:
            float: The diameter in meters.
        """
        return self._diameter_m

    @diameter_m.setter
    def diameter_m(self, value: float) -> None:
        """Setter for the diameter in meters.

        Args:
            value (float): The diameter in meters to set.
        """
        self._diameter_ft = value * 3.28084
        self._diameter_m = value

    @property
    def diameter_ft(self) -> float:
        """Getter for the diameter in feet.

        Returns:
            float: The diameter in feet.
        """
        return self._diameter_ft

    @diameter_ft.setter
    def diameter_ft(self, value: float) -> None:
        """Setter for the diameter in feet.

        Args:
            value (float): The diameter in feet to set.
        """
        self._diameter_m = value / 3.28084
        self._diameter_ft = value

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
    def files_timestamp(self) -> datetime.time:
        """Getter for the files timestamp.

        Returns:
            datetime.time: The files timestamp.
        """
        return self._files_timestamp

    @files_timestamp.setter
    def files_timestamp(self, value: datetime.time) -> None:
        """Setter for the files timestamp.

        Args:
            value (datetime.time): The files timestamp to set.
        """
        self._files_timestamp = value

    @property
    def id(self) -> str:
        """Getter for the id.

        Returns:
            str: The id.
        """
        return self._id

    def create_output_file(self, output_path) -> str:
        """Create the output file.

        Creates the output file with all attributes and sets the path and returns the path.

        Args:
            output_path (str): The path of the output file.

        Returns:
            str: The path of the output file.
        """
        with open(output_path + str(self._timestamp), "w") as file:
            file.write("The Result path: {}\n".format(self._path))
            file.write("The Result timestamp: {}\n".format(self._timestamp))
            file.write("The Result latitude: {}\n".format(self._lat))
            file.write("The Result longitude: {}\n".format(self._lon))
            file.write("The Result type: {}\n".format(self._type))
            file.write("The Result confidence: {}\n".format(self._confidence))
            file.write("The Result depth in meters: {}\n".format(self._depth_m))
            file.write("The Result depth in feet: {}\n".format(self._depth_ft))
            file.write("The Result diameter in meters: {}\n".format(self._diameter_m))
            file.write("The Result diameter in feet: {}\n".format(self._diameter_ft))
            file.write("The Result audio file: {}\n".format(self._audio_file))
            file.write("The Result location file: {}\n".format(self._location_file))
            file.write("The Result files timestamp: {}\n".format(self._files_timestamp))
        self._path = output_path
        return output_path

    def __str__(self) -> str:
        """Return the string representation of the object.

        Provides a human-readable string describing it.

        Returns:
            str: String representation of it.
        """
        return "{} {} {}".format("The Result path:", self._path, self._timestamp)

    def __eq__(self, value: object) -> bool:
        """Check the equality of this with another object.

        Two are considered equal if they have the same attributes

        Args:
            value (object): The object to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        if isinstance(value, Result):
            return (self._id == value.id and
                    self._timestamp == value.timestamp and
                    self._lat == value.lat and
                    self._lon == value.lon and
                    self._type == value.type and
                    self._confidence == value.confidence and
                    self._depth_m == value.depth_m and
                    self._depth_ft == value.depth_ft and
                    self._diameter_m == value.diameter_m and
                    self._diameter_ft == value.diameter_ft and
                    self._audio_file == value.audio_file and
                    self._location_file == value.location_file and
                    self._files_timestamp == value.files_timestamp)
        else:
            return False
