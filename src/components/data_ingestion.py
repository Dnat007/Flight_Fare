import os
import sys
from src.exception import CustomException

from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from dataclasses import dataclass
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.xlsx")
    test_data_path: str = os.path.join('artifacts',"test.xlsx")
    raw_data_path: str = os.path.join('artifacts',"raw.xlsx")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):    
        logging.info("Enter into the data ingestion method")
        try:
            df =pd.read_excel("notebook\data\Data_Train.xlsx")
            logging.info("Read the dataset in a easy manner")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_excel(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("initiated the train test split")
            train_set,test_set = train_test_split(df,test_size=0.25,random_state=35)
            
            train_set.to_excel(self.ingestion_config.train_data_path,index = False,header =True)
            
            test_set.to_excel(self.ingestion_config.test_data_path,index = False,header =True)
            
            logging.info("data ingestion is completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            ) 
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr , test_arr,_ = data_transformation.initialize_data_transformation(train_data,test_data)
    
    Model_trainer = ModelTrainer()
    print(Model_trainer.initiate_model_trainer(train_arr,test_arr))
    