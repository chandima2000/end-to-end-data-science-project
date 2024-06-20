# Reading data from the particular database
# After completing data_ingestion, data_transformation happen

import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging


# This class is responsible for where the test data should save,
# where the train data should save,
# where the raw data should save

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifact',"train.csv")
    test_data_path: str=os.path.join('artifact',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


