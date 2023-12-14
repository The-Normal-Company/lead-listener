"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import pytest
from src.leadlistener.data.input.LocationFile import LocationFile
import datetime
import csv
from unittest.mock import mock_open, patch


class TestLocationFile:
    """Test class for LocationFile."""

    def setup_method(self):
        """Setup method called before each test method."""
        self.location_file = LocationFile()

    def test_initial_state(self):
        """Test the initial state of the LocationFile."""
        assert self.location_file.path == ""
        assert isinstance(self.location_file.id, int)
        assert self.location_file.timestamp is None

    def test_path_setter_and_getter(self):
        """Test the setter and getter for path."""
        test_path = "test/path"
        self.location_file.path = test_path
        assert self.location_file.path == test_path

    def test_timestamp_setter_and_getter(self):
        """Test the setter and getter for timestamp."""
        self.location_file.timestamp = datetime.datetime(2023, 1, 1, 12, 0)
        assert self.location_file.timestamp == datetime.datetime(2023, 1, 1, 12, 0)

    def test_str_representation(self):
        """Test the string representation of the object."""
        self.location_file.path = "test/path"
        self.location_file.timestamp = datetime.datetime(2023, 1, 1, 12, 0)
        expected_str = "The Location Input File path: test/path 2023-01-01 12:00:00"
        assert str(self.location_file) == expected_str

    def test_equality(self):
        """Test the equality method."""
        file1 = LocationFile()
        file2 = LocationFile()
        file1.path = "path1"
        file2.path = "path1"
        file1.timestamp = datetime.datetime(2023, 1, 1, 12, 0)
        file2.timestamp = datetime.datetime(2023, 1, 1, 12, 0)
        assert file1 == file2

        file2.path = "path2"
        assert not file1 == file2

    @patch("builtins.open", new_callable=mock_open, read_data="id,lat,lon\n1,34.0522,-118.2437")
    def test_read_from_csv(self, mock_file):
        """Test the read_from_csv method."""
        self.location_file.path = "test.csv"
        lat = self.location_file.lat
        lon = self.location_file.lon
        assert lat == 34.0522
        assert lon == -118.2437
