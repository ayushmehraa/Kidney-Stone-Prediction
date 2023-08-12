import os
import sys
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train,y_train)

            y_train_pred_proba = model.predict_proba(X_train)[:,1]

            y_test_pred_proba = model.predict_proba(X_test)[:,1]

            train_model_roc_score = roc_auc_score(y_train, y_train_pred_proba)

            test_model_roc_score = roc_auc_score(y_test, y_test_pred_proba)

            report[list(models.keys())[i]] = test_model_roc_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    
    except Exception as e :
        return CustomException(e, sys)
    

            