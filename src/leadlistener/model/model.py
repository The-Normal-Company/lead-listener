"""LeadListener Project.

Find the lead.

Author: Tyler Bolz
Version: 0.1
"""

import os
import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from typing import List


class Model():
    """Model Class.

    Represents a model for classifying types of pipes based on audio features.
    """

    def __init__(self) -> None:
        """Initializes a new instance of Model.
        """
        self.clf = RandomForestClassifier()
        self.train_classifier()

    def extract_features(self, audio_file: str) -> np.ndarray:
        """Extracts MFCC features from an audio file.

        Args:
            audio_file (str): The path to the audio file.

        Returns:
            np.ndarray: The extracted features.
        """
        y, sr = librosa.load(audio_file)
        mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
        return mfccs

    def extract_features_from_directory(self, directory_path: str) -> List[np.ndarray]:
        """Extracts features from all audio files in a directory.

        Args:
            directory_path (str): The path to the directory containing audio files.

        Returns:
            List[np.ndarray]: A list of feature arrays extracted from the audio files.
        """
        features_list = []
        for filename in os.listdir(directory_path):
            if filename.endswith(".wav"):
                file_path = os.path.join(directory_path, filename)
                features = self.extract_features(file_path)
                features_list.append(features)
        return features_list

    def train_classifier(self) -> None:
        """Pre-trains the RandomForestClassifier with the provided training data.
        """
        lead_data_directory = r"src\leadlistener\model\training\raw\lead"
        steel_data_directory = r"src\leadlistener\model\training\raw\steel"
        pvc_data_directory = r"src\leadlistener\model\training\raw\pvc"

        lead_data_features = self.extract_features_from_directory(lead_data_directory)
        steel_data_features = self.extract_features_from_directory(steel_data_directory)
        pvc_data_features = self.extract_features_from_directory(pvc_data_directory)

        X = lead_data_features + steel_data_features + pvc_data_features
        y = [0] * len(lead_data_features) + [1] * len(steel_data_features) + [2] * len(pvc_data_features)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.clf.fit(X_train, y_train)

    def predict_pipe_type(self, audio_file: str) -> str:
        """Predicts the pipe type for a given audio file.

        Args:
            audio_file (str): The path to the audio file to be classified.

        Returns:
            str: The predicted pipe type.
        """
        features = self.extract_features(audio_file)
        prediction = self.clf.predict([features])[0]
        pipe_mapping = {0: "lead", 1: "steel", 2: "pvc"}
        return pipe_mapping[prediction]
