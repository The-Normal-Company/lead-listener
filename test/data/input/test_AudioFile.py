"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import pytest
from src.leadlistener.data.input.AudioFile import AudioFile
import datetime


class TestAudioFile:
    """Test class for AudioFile."""

    def setup_method(self):
        """Setup method called before each test method."""
        self.audio_file = AudioFile()

    def test_initial_state(self):
        """Test the initial state of the AudioFile."""
        assert self.audio_file.path == ""
        assert isinstance(self.audio_file.id, int)
        assert self.audio_file.timestamp is None

    def test_path_setter_and_getter(self):
        """Test the setter and getter for path."""
        test_path = "test/path"
        self.audio_file.path = test_path
        assert self.audio_file.path == test_path

    def test_timestamp_setter_and_getter(self):
        """Test the setter and getter for timestamp."""
        self.audio_file.timestamp = datetime.datetime(2023, 1, 1, 12, 0)
        assert self.audio_file.timestamp == datetime.datetime(2023, 1, 1, 12, 0)

    def test_str_representation(self):
        """Test the string representation of the object."""
        self.audio_file.path = "test/path"
        self.audio_file.timestamp = datetime.datetime(2023, 1, 1, 12, 0)
        expected_str = "The Audio Input File path: test/path 2023-01-01 12:00:00"
        assert str(self.audio_file) == expected_str

    def test_equality(self):
        """Test the equality method."""
        file1 = AudioFile()
        file2 = AudioFile()
        file1.path = "path1"
        file2.path = "path1"
        file1.timestamp = datetime.datetime(2023, 1, 1, 12, 0)
        file2.timestamp = datetime.datetime(2023, 1, 1, 12, 0)
        assert file1 == file2

        file2.path = "path2"
        assert not file1 == file2
