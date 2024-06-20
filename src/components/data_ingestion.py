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
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the dataset from csv file. This can be from database, api
            df=pd.read_csv('notebook/data/students.csv')
            logging.info("Data loaded successfully as data frame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            # Get the data from the data source and insert it into the csv file.
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("create the raw dataset from the data frame")

            train_set, test_set=train_test_split(df,test_size=0.2,random_state=42)
            logging.info("Train, Test split initiated")

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            logging.info("create train dataset successfully")

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("create test dataset successfully")

            logging.info("DataIngestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.info("Data Ingestion failed!")
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()