from flask import Flask,request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.piplines.predict_pipline import CustomData 
from src.piplines.predict_pipline import PredictPipline 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predictdata', methods=["GET","POST"])
def predict_datapoint():
    if request.method=="GET":
        return render_template("predictdata.html")

    else:
        data = CustomData(
            Airline = request.form.get('Airline'),
            Source = request.form.get('Source'),
            Destination = request.form.get('Destination'),
            Total_Stops = request.form.get('Total_Stops'),
            
            journey_day = int(request.form.get('journey_day')),
            journey_month = int(request.form.get('journey_month')),
            Dep_Time_hour = int(request.form.get('Dep_Time_hour')),
            Dep_Time_min = int(request.form.get('Dep_Time_min')),
            Arrival_Time_hour = int(request.form.get('Arrival_Time_hour')),
            Arrival_Time_min = int(request.form.get('Arrival_Time_min')), 
            Dur_hours = int(request.form.get('Dur_hours')), 
            Dur_mins = int(request.form.get('Dur_mins'))
        )
        pred_df = data.get_data_as_data_frame()
        print(data)
        print(pred_df)

        predict_pipline = PredictPipline()
        results = predict_pipline.predict(pred_df)

        return render_template("predictdata.html",pred_df=pred_df, results=results)
    
if __name__ == "__main__":
    # app = Flask(__name__, template_folder='/template')
    app.run(host = "0.0.0.0",debug = True, port=8080)