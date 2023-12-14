"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MapPanel(tk.Frame):
    """MapPanel.

    Represents the map panel using Matplotlib for plotting.
    """

    def __init__(self, master, lat, lon):
        """The constructor for MapPanel.

        Args:
            master (tk.Frame): The master widget.
            lat (float): The latitude.
            lon (float): The longitude.
        """
        super().__init__(master)
        self.lat = lat
        self.lon = lon
        
        self.fig, self.ax = plt.subplots()
        
        self.ax.scatter(self.lat, self.lon, color='blue', marker='o')  # You can change the color and marker style

        self.ax.set_xlabel('Latitude')
        self.ax.set_ylabel('Longitude')
        self.ax.set_title('Map Coordinates')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill="both", expand=True)

        self.canvas.draw()