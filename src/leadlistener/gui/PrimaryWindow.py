"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import tkinter as tk
from src.starfleetsubs.gui.MenuPanel import MenuPanel
from src.starfleetsubs.gui.OrderPanel import OrderPanel
from src.starfleetsubs.data.Item import Item
from src.starfleetsubs.gui.ParentPanel import ParentPanel


class PrimaryWindow(tk.Tk, ParentPanel):
    """Primary Window.

    This is the primary window for the program.
    """

    def __init__(self) -> None:
        """Primary Window init"""
        tk.Tk.__init__(self)
        self.minsize(width=800, height=600)
        self.title("Starfleet Subs")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=2)

        self.__main = None
        self.__sidebar = OrderPanel(self)
        self.load_order_panel()

        self.__sidebar.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

    def load_order_panel(self) -> None:
        """Load Order Panel."""
        self.load_panel(MenuPanel(self, self.__sidebar))

    def load_panel(self, panel):
        """Load Panel.

        Args:
            panel: The panel to load.
        """
        if self.__main is not None:
            self.__main.destroy()
        self.__main = panel
        self.__main.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    def save_item(self, item: Item) -> None:
        """Save Item.

        Args:
            item: The item to save.
        """
        self.__sidebar.save_item(item)