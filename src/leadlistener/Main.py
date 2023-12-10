"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

from typing import List
from src.leadlistener.gui.PrimaryWindow import PrimaryWindow


class Main:
    """Main Class."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Main method."""
        PrimaryWindow().mainloop()
