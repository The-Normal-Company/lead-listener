"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from src.leadlistener.data.input.AudioFile import AudioFile
from src.leadlistener.data.input.LocationFile import LocationFile
import os
import shutil


class InputPanel(tk.Frame):
    """Input Panel.

    For uploading Location and Audio files.
    """

    def __init__(self, master=None, save_callback=None, bg="#f0f0f0", highlightbackground="gray", highlightthickness=1):
        """Constructor for InputPanel."""
        super().__init__(master)
        self.master = master
        self.save_callback = save_callback

        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12), padding=5)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.location_label = ttk.Label(self, text="Upload Location File")
        self.location_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.location_button = ttk.Button(self, text="Browse...", command=self.upload_location_file)
        self.location_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.audio_label = ttk.Label(self, text="Upload Audio File")
        self.audio_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.audio_button = ttk.Button(self, text="Browse...", command=self.upload_audio_file)
        self.audio_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.save_button = ttk.Button(self, text="Submit", command=self.save_files)
        self.save_button.grid(row=2, column=0, columnspan=2, pady=20)

    def upload_location_file(self):
        """Upload Location File."""
        self.location_file_path = filedialog.askopenfilename()
        self.location_label.config(text=f"Location File: {os.path.basename(self.location_file_path)}")

    def upload_audio_file(self):
        """Upload Audio File."""
        self.audio_file_path = filedialog.askopenfilename()
        self.audio_label.config(text=f"Audio File: {os.path.basename(self.audio_file_path)}")

    def save_files(self):
        """Save files and create LocationFile and AudioFile instances."""
        if hasattr(self, 'location_file_path') and hasattr(self, 'audio_file_path'):
            save_path = "src/leadlistener/data/input/raw"
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            shutil.copy(self.location_file_path, save_path)
            shutil.copy(self.audio_file_path, save_path)

            self.location_file = LocationFile()
            self.location_file.path = os.path.join(save_path, os.path.basename(self.location_file_path))

            self.audio_file = AudioFile()
            self.audio_file.path = os.path.join(save_path, os.path.basename(self.audio_file_path))

            if self.save_callback:
                self.save_callback()
        else:
            tk.messagebox.showwarning("Warning", "Please upload both files before saving.")
