import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd
import os
from dotenv import load_dotenv

from src.Components.data_transformation import DataTransformation
from src.Components.data_transformation import DataTransformationConfig
from src.Components.model_trainer import ModelTrainer
from src.Components.model_trainer import ModelTrainerConfig


@dataclass # we can dirctly define our class variabel with dataclass without using __init__
class DataInegstionConfig:

    '''A class to take some inpute for data ingestion (for example like path of saving train data, path of saving test data, path of saving raw data etc.) Any input required for data Ingestion will taken through DataIngestinoConfig class
    '''
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataInegstionConfig()
    
    def initate_data_ingestion(self):
        logging.info("Entered the data ingestion or component")
        try:
            load_dotenv()
            secure_bundle = os.getenv('secure_bundle')
            client_id = os.getenv('client_id')
            client_secret = os.getenv('client_secret')
            cloud_config= {
                    'secure_connect_bundle': secure_bundle  
            }
            auth_provider = PlainTextAuthProvider(client_id, client_secret)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            df = pd.DataFrame(list(session.execute('SELECT * FROM stroke.data;')))

            
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df, test_size=0.20, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of data is completed")
            return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
                )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initate_data_ingestion()
    data_transformation = DataTransformation()
    train_array,test_array, preprocessor_path = data_transformation.initiate_data_transformation(train_data,test_data)
    modeltrainer = ModelTrainer()
    print(modeltrainer.initate_model_trainer(train_array=train_array,test_array=test_array,preprocessor_path=preprocessor_path))

