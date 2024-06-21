### How to handle one hot encoding, label encoding
### Do feature Engineering, Data cleaning, Pipelining

import sys
import os
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer 
from dataclasses import dataclass
from sklearn.impute import SimpleImputer 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
     def __init__(self):
        self.data_transformation_config=DataTransformationConfig() # create object

    ## Create all pickle files
     def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            # pipeline for the Numerical data
            num_pipeline= Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="median")), # fill the missing values using "median"
                ("scaler",StandardScaler()) # Standardization
                ]

            )
            logging.info("Numerical data Standard Scaling is completed.")


            # pipeline for the Categorical data
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")), # fill the missing values using "mode"
                ("one_hot_encoder",OneHotEncoder()), # Encoding
                ("scaler",StandardScaler())  # Standardization
                ]

            )
            logging.info("Categorical data encoding is completed.")


            # combine the numerical pipeline and categorical pipeline together
            preprocessor=ColumnTransformer(
                [
                    ("numerical_pipeline",num_pipeline,numerical_columns),
                    ("categorical_pipeline",cat_pipeline,categorical_columns)
                ]
            )

            logging.info("successfully combined the numerical and categorical pipelines together")
            return preprocessor
            
        except CustomException as e:
            logging.info("DataTransformation is failed!")
            raise CustomException(e, sys)

