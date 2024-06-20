### How to handle one hot encoding, label encoding
### Do feature Engineering, Data cleaning

import sys
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer 
from dataclasses import dataclass
from sklearn.impute import SimpleImputer 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging