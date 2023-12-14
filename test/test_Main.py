"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""
import pytest
from src.leadlistener.Main import Main
from src.leadlistener.gui.PrimaryWindow import PrimaryWindow
from unittest.mock import MagicMock, patch


class TestMain:
    """Test class for Main."""

    @patch('src.leadlistener.gui.PrimaryWindow.PrimaryWindow')
    def test_main(self, mock_primary_window):
        """Test the main method."""
        mock_window_instance = MagicMock()
        mock_primary_window.return_value = mock_window_instance

        Main.main([])

        mock_primary_window.assert_called_once()
        mock_window_instance.mainloop.assert_called_once()
