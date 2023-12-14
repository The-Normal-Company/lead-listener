"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import pytest
from src.leadlistener.gui.output.OutputPanel import OutputPanel
from src.leadlistener.gui.output.MapPanel import MapPanel
from tkinter import Tk, StringVar
from unittest.mock import MagicMock, patch

class TestOutputPanel:
    """Test class for OutputPanel."""

    def setup_method(self):
        """Setup method called before each test method."""
        self.root = Tk()
        self.lat = 40.7128
        self.lon = -74.0060
        self.text_variable = StringVar()
        self.output_panel = OutputPanel(master=self.root, lat=self.lat, lon=self.lon, text_variable=self.text_variable)

    def teardown_method(self):
        """Teardown method called after each test method."""
        self.root.destroy()

    def test_initialization(self):
        """Test the initialization of OutputPanel."""
        assert self.output_panel.lat == self.lat
        assert self.output_panel.lon == self.lon
        assert self.output_panel.text_variable == self.text_variable
        assert isinstance(self.output_panel.map_panel, MapPanel)
        assert self.output_panel.map_panel.pack_info()["side"] == "top"
        assert self.output_panel.text_label.cget("textvariable") == str(self.text_variable)
