import os
import sys
import logging
from src.exception import customException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation

logger = logging.getLogger(__name__)

## Intitialize the Data Ingetion Configuration
@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('data','gemstone.csv')


## create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logger.info('Data Ingestion methods Starts')
        try:
        

            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logger.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.read_csv(self.ingestion_config.raw_data_path,index=False)
            logger.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logger.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logger.info('Exception occured at Data Ingestion stage')
            raise customException(e,sys)
        
        




