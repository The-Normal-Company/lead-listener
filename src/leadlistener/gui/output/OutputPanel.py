"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.leadlistener.gui.output.MapPanel import MapPanel


class OutputPanel(tk.Frame):
    """OutputPanel.

    Represents the output panel.
    """

    def __init__(self, master, lat, lon, text_variable):
        """Initialize the OutputPanel with a master widget, latitude, longitude, and a text variable.

        Args:
            master (tk.Frame): The master widget.
            lat (float): The latitude.
            lon (float): The longitude.
            text_variable (tk.StringVar): The text variable.
        """
        super().__init__(master)
        self.lat = lat
        self.lon = lon
        self.text_variable = text_variable

        self.map_panel = MapPanel(self, self.lat, self.lon)
        self.map_panel.pack(side="top", fill="both", expand=True)

        self.text_label = ttk.Label(self, textvariable=self.text_variable, wraplength=500)
        self.text_label.pack(side="bottom", fill="both", expand=True)
