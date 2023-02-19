import csv
import torch
import numpy as np
import pandas as pd

from torch.utils.data import Dataset


class TemplateDataset(Dataset):
    def __init__(self) -> None:
        """ Initialize file path or list of file names"""
        pass


    def __getitem__(self, idx):
        """
        1. Read one data from file (e.g. using numpy.fromfile, PIL.Image.open).
        2. Preprocess the data (e.g. torchvision.Transform).
        3. 3. Return a data pair (e.g. image and label).
        :param idx:
        """
        pass

    def __len__(self):
        """returns the size of the dataset."""
        return None

