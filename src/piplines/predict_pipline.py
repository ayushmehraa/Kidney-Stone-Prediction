import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os
class PredictPipline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict_proba(data_scaled)[:,1]
            return preds
        except Exception as e:
            return CustomException(e, sys)
    
class CustomData:
    def __init__(self,
        gravity : float,
        ph:float,	
        osmo:int,
        cond : float,	
        urea : int, 
        calc: float):

        self.gravity = gravity

        self.ph = ph

        self.osmo = osmo

        self.cond = cond

        self.urea = urea

        self.calc = calc
        
    def get_data_as_data_frame(self):
        try:
             custom_data_input_dict = {
                "calc": [self.calc],
                "cond": [self.cond],
                "gravity": [self.gravity],
                "osmo": [self.osmo],
                "ph": [self.ph],
                "urea": [self.urea]
            }
            
             return pd.DataFrame(custom_data_input_dict)
       
        except Exception as e:
            return CustomException(e,sys)