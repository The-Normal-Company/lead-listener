"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import pytest
from src.leadlistener.gui.output.MapPanel import MapPanel
from tkinter import Tk
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt


class TestMapPanel:
    """Test class for MapPanel."""

    def setup_method(self):
        """Setup method called before each test method."""
        self.root = Tk()
        self.lat = 40.7128
        self.lon = -74.0060
        self.map_panel = MapPanel(master=self.root, lat=self.lat, lon=self.lon)

    def teardown_method(self):
        """Teardown method called after each test method."""
        plt.close('all')
        self.root.destroy()

    def test_initialization(self):
        """Test the initialization of MapPanel."""
        assert self.map_panel.lat == self.lat
        assert self.map_panel.lon == self.lon
        assert hasattr(self.map_panel, 'fig')
        assert hasattr(self.map_panel, 'ax')
        assert hasattr(self.map_panel, 'canvas')

    def test_plotting(self):
        """Test the plotting functionality."""
        assert self.map_panel.ax.get_xlabel() == 'Latitude'
        assert self.map_panel.ax.get_ylabel() == 'Longitude'
        assert self.map_panel.ax.get_title() == 'Map Coordinates'
