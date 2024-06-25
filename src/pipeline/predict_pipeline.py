import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object  ## Load the pickel file
from src.utils import logging
class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):

        try:
            model_path='artifacts/model.pkl'
            preprocessor_path='artifacts/preprocessor.pkl' # Responsible for handling categorical features, feature scaling
            model=load_object(file_path=model_path) # load model in read byte mode
            preprocessor=load_object(file_path=preprocessor_path) # load preprocessor in read byte mode
            data_scaled=preprocessor.transform(features) # Preprocess the data using preprocessor.pkl
            prediction=model.predict(data_scaled)  # Give preprocessed data to the model to predict
            logging.info("returned the prediction")
            return prediction
        
        except Exception as e:
            logging.info("Error, while making prediction in PredictPipeline!")
            raise CustomException(e,sys)

class CustomData:

    # This is responsible for handling data
    # which are coming from the Frontend
    def __init__(self,
        gender:str,
        race_ethnicity:str,
        parental_level_of_education:str,
        lunch:str,
        test_preparation_course:str,
        reading_score:int,
        writing_score:int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    # This return the data as Data-Frame
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            logging.info("returned data as Data Frame")
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            logging.info("Error, getting data as data frame.")
            raise CustomException(e,sys)
    