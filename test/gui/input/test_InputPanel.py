"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import pytest
from src.leadlistener.gui.input.InputPanel import InputPanel
from tkinter import Tk
import os
from unittest.mock import patch, MagicMock
from src.leadlistener.data.input.LocationFile import LocationFile
from src.leadlistener.data.input.AudioFile import AudioFile


class TestInputPanel:
    """Test class for InputPanel."""

    def setup_method(self):
        """Setup method called before each test method."""
        self.root = Tk()
        self.input_panel = InputPanel(master=self.root)

    def teardown_method(self):
        """Teardown method called after each test method."""
        self.root.destroy()

    @patch('tkinter.filedialog.askopenfilename')
    def test_upload_location_file(self, mock_askopenfilename):
        """Test upload_location_file method."""
        mock_askopenfilename.return_value = '/path/to/locationfile.csv'
        self.input_panel.upload_location_file()
        assert hasattr(self.input_panel, 'location_file_path')
        assert self.input_panel.location_file_path == '/path/to/locationfile.csv'

    @patch('tkinter.filedialog.askopenfilename')
    def test_upload_audio_file(self, mock_askopenfilename):
        """Test upload_audio_file method."""
        mock_askopenfilename.return_value = '/path/to/audiofile.wav'
        self.input_panel.upload_audio_file()
        assert hasattr(self.input_panel, 'audio_file_path')
        assert self.input_panel.audio_file_path == '/path/to/audiofile.wav'

    @patch('shutil.copy')
    @patch('os.path.exists')
    @patch('os.makedirs')
    def test_save_files(self, mock_makedirs, mock_exists, mock_copy):
        """Test save_files method."""
        self.input_panel.location_file_path = '/path/to/locationfile.csv'
        self.input_panel.audio_file_path = '/path/to/audiofile.wav'
        mock_exists.return_value = False
        self.input_panel.save_files()

        mock_makedirs.assert_called_with("src/leadlistener/data/input/raw")
        mock_copy.assert_any_call('/path/to/locationfile.csv', 'src/leadlistener/data/input/raw')
        mock_copy.assert_any_call('/path/to/audiofile.wav', 'src/leadlistener/data/input/raw')
        assert isinstance(self.input_panel.location_file, LocationFile)
        assert isinstance(self.input_panel.audio_file, AudioFile)
