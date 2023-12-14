"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import pytest
from src.leadlistener.data.output.Result import Result
import datetime
from unittest.mock import patch, mock_open


class TestResult:
    """Test class for Result."""

    def setup_method(self):
        """Setup method called before each test method."""
        self.result = Result()

    def test_initial_state(self):
        """Test the initial state of the Result."""
        assert self.result.lat == 0.0
        assert self.result.lon == 0.0

    def test_setters_and_getters(self):
        """Test the setters and getters for each property."""
        self.result.lat = 34.0522
        assert self.result.lat == 34.0522

    def test_create_output_file(self):
        """Test the create_output_file method."""
        output_path = "test_output.txt"
        with patch("builtins.open", new_callable=mock_open) as mock_file:
            returned_path = self.result.create_output_file(output_path)
            mock_file.assert_called_with(output_path + str(self.result.timestamp), "w")
            assert returned_path == output_path

    def test_str_representation(self):
        """Test the string representation of the object."""
        self.result.lat = 34.0522
        expected_str = "The Result path:  34.0522"
        assert str(self.result) == expected_str

    def test_equality(self):
        """Test the equality method."""
        result1 = Result()
        result2 = Result()
        result1.lat = 34.0522
        result2.lat = 34.0522
        assert result1 == result2

        result2.lat = 40.7128
        assert not result1 == result2
