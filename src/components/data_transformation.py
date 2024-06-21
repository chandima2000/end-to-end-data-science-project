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
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
     def __init__(self):
        self.data_transformation_config=DataTransformationConfig() # create object

    ## Data Preprocessing
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
                ("scaler",StandardScaler(with_mean=False)) # Standardization
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
    
     ## Starting the data transformation
     def initiate_data_transformation(self,train_path,test_path):   ### train_path,test_path coming from the data_ingestion.py

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Read train and test data is completed.")

            logging.info("Obtaining preprocessing object")
            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                "Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]


            # This function is coming from the utils file.
            # Use to save .pkl files
            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj # This is what we want to save

            )
            logging.info("Created the preprocessor.pkl file.")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        
        except Exception as e:
            logging.info("Error, while initiating data transformation!")
            raise CustomException(e,sys)