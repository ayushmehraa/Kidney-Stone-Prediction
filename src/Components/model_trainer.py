import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost 
from sklearn.metrics import roc_auc_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initate_model_trainer(self,train_array,test_array, preprocessor_path):
        try:
            logging.info("Spliting training and testing input data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Logistic Regression": LogisticRegression(),
                "SVC": SVC(probability=True),
                "Random Forest Classifier": RandomForestClassifier(),
                "AdaBoost Classifier": AdaBoostClassifier(),
                "xgboost Classifier": xgboost.XGBClassifier(),
                "Decision Tree": DecisionTreeClassifier()
            }

            model_report:dict=evaluate_models(X_train = X_train, y_train = y_train, X_test = X_test, y_test = y_test, models = models)

            # To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

           # To get best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            
            logging.info("Best model found on both training set and test set")
            
            save_object(file_path = self.model_trainer_config.trained_model_file_path, obj = best_model)

            predicted_prob = best_model.predict_proba(X_test)[:,1]

            roc = roc_auc_score(y_test, predicted_prob)
            
            return roc


        except Exception as e:
            raise CustomException(e,sys)
