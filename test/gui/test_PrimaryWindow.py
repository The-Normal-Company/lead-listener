"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import pytest
from src.leadlistener.gui.PrimaryWindow import PrimaryWindow
from src.leadlistener.gui.input.InputPanel import InputPanel
from src.leadlistener.gui.output.OutputPanel import OutputPanel
from unittest.mock import patch, MagicMock
from src.leadlistener.model.Model import Model
from src.leadlistener.data.output.Results import Results


class TestPrimaryWindow:
    """Test class for PrimaryWindow."""

    def setup_method(self):
        """Setup method called before each test method."""
        self.primary_window = PrimaryWindow()

    def test_initialization(self):
        """Test the initialization of the PrimaryWindow."""
        assert isinstance(self.primary_window._model, Model)
        assert isinstance(self.primary_window._results, Results)
        assert self.primary_window.input_panel is not None
        assert self.primary_window.output_panel is not None

    @patch('src.leadlistener.gui.input.InputPanel.InputPanel')
    @patch('src.leadlistener.gui.output.OutputPanel.OutputPanel')
    def test_load_panels(self, mock_output_panel, mock_input_panel):
        """Test the loading of input and output panels."""
        self.primary_window.load_input_panel()
        mock_input_panel.assert_called_once()
        self.primary_window.load_output_panel()
        mock_output_panel.assert_called_once()

    @patch('src.leadlistener.model.Model.predict_pipe_type', return_value="Prediction Result")
    def test_save(self, mock_predict_pipe_type):
        """Test the save method."""
        self.primary_window.input_panel = MagicMock()
        self.primary_window.input_panel.location_file.path = "location.csv"
        self.primary_window.input_panel.audio_file.path = "audio.wav"

        self.primary_window.save()

        mock_predict_pipe_type.assert_called_with("audio.wav")
        assert len(self.primary_window._results.results) == 1
        assert self.primary_window._results.results[0].audio_file == "audio.wav"
        assert self.primary_window._results.results[0].location_file == "location.csv"
