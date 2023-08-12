import os
import sys
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    
    except Exception as e :
        return CustomException(e, sys)
    
def drop_na(df):
    df.dropna(inplace=True)    

def jouney_tranformation(df):
    df['journey_day'] = pd.to_datetime(df["Date_of_Journey"]).dt.day
    df['journey_month']= pd.to_datetime(df["Date_of_Journey"]).dt.month
    df.drop('Date_of_Journey', axis=1, inplace=True)

def arival_time_tranformation(df):
    df["Arrival_Time_hour"] = pd.to_datetime(df["Arrival_Time"]).dt.hour
    df["Arrival_Time_min"] = pd.to_datetime(df["Arrival_Time"]).dt.minute
    df.drop("Arrival_Time",axis=1,inplace=True)

def dep_time_transformation(df):
    df["Dep_Time_hour"] = pd.to_datetime(df["Dep_Time"]).dt.hour
    df["Dep_Time_min"] = pd.to_datetime(df["Dep_Time"]).dt.minute
    df.drop("Dep_Time",axis=1,inplace=True)

def duration_tranformation(df):
    def dur_hour(x):
        return x.split(" ")[0][0:-1]

    def dur_minutes(x):
        return x.split(" ")[1][0:-1]

    duration = list(df['Duration'])
    for i in range(len(duration)):
        if len(duration[i].split(" "))==2:
            pass
        else:
            if "h" in duration[i]:
                duration[i] = duration[i]+" 0m"
            else:
                duration[i] = "0h "+duration[i] 
    df['Duration'] = duration

    # Extracting Duration Hours
    df["Dur_hours"] = df["Duration"].apply(dur_hour).astype(int)
    # Extracting Duration Minutes
    df["Dur_mins"] = df["Duration"].apply(dur_minutes).astype(int)
    # Dropping Duration column
    df.drop(columns=["Duration"],inplace=True)

def replace_vlaues(df):
    df.Airline.replace("Trujet","other",inplace=True)
    df.Airline.replace("Vistara Premium economy","other",inplace=True)
    df.Airline.replace("Jet Airways Business","other",inplace=True)
    df.Airline.replace("Multiple carriers Premium economy","other",inplace=True)
    df.Total_Stops.replace("4 stops","3 stops",inplace=True)


def drop_features(df):
    df.drop(columns=["Additional_Info","Route"],inplace=True)
            