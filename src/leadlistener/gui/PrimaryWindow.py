"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import tkinter as tk
from src.leadlistener.gui.input.InputPanel import InputPanel
from src.leadlistener.model.Model import Model
from src.leadlistener.gui.output.OutputPanel import OutputPanel
from src.leadlistener.data.output.Result import Result
from src.leadlistener.data.output.Results import Results


class PrimaryWindow(tk.Tk):
    """Primary Window.

    This is the primary window for the program, showing the InputPanel.
    """

    def __init__(self) -> None:
        """Primary Window init"""
        super().__init__()
        self._model = Model()
        self._results = Results()
        self.minsize(width=800, height=600)
        self.title("Lead Listener")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.input_panel = None
        self.output_panel = None

        self.load_input_panel()
        self.load_output_panel()

    def load_input_panel(self) -> None:
        """Load Input Panel."""
        if self.input_panel is not None:
            self.input_panel.destroy()
        self.input_panel = InputPanel(self, save_callback=self.save)
        self.input_panel.config(highlightbackground="black", highlightthickness=1)  # Add outline        
        self.input_panel.grid(row=0, column=0, sticky="nsew")

    def load_output_panel(self, text="Waiting...", lat=0.0, lon=0.0) -> None:
        """Load Output Panel."""
        if self.output_panel is not None:
            self.output_panel.destroy()
        self.output_panel = OutputPanel(self, lat=lat, lon=lon, text_variable=tk.StringVar(value=text))
        self.output_panel.config(highlightbackground="black", highlightthickness=1)  # Add outline
        self.output_panel.grid(row=0, column=1, sticky="nsew")

    def save(self) -> None:
        """Save."""
        self.load_output_panel(text="Processing...")
        location_file = self.input_panel.location_file.path
        audio_file = self.input_panel.audio_file.path
        result = self._model.predict_pipe_type(audio_file)
        self.load_output_panel(text=result, lat=self.input_panel.location_file.lat, lon=self.input_panel.location_file.lon)
        result = Result()
        result.lat = self.input_panel.location_file.lat
        result.lon = self.input_panel.location_file.lon
        result.type = result
        result.confidence = 1.0
        result.audio_file = audio_file
        result.location_file = location_file
        result.files_timestamp = self.input_panel.location_file.timestamp
        self._results.add_result(result)
