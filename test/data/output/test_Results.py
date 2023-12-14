"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import pytest
from src.leadlistener.data.output.Results import Results
from src.leadlistener.data.output.Result import Result
import datetime


class TestResults:
    """Test class for Results."""

    def setup_method(self):
        """Setup method called before each test method."""
        self.results = Results()

    def test_initial_state(self):
        """Test the initial state of the Results."""
        assert len(self.results.results) == 0

    def test_setters_and_getters(self):
        """Test the setters and getters for each property."""
        self.results.audio_file = "audio.wav"
        assert self.results.audio_file == "audio.wav"

    def test_add_and_remove_result(self):
        """Test adding and removing a result."""
        result = Result()
        self.results.add_result(result)
        assert len(self.results.results) == 1
        assert self.results.results[0] == result

        self.results.remove_result(result)
        assert len(self.results.results) == 0

    def test_equality(self):
        """Test the equality method."""
        results1 = Results()
        results2 = Results()
        result = Result()
        results1.add_result(result)
        results2.add_result(result)
        assert results1 == results2

        results2.remove_result(result)
        assert not results1 == results2
