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
            gravity = int(request.form.get('gravity')),
            ph = int(request.form.get('ph')),
            osmo = int(request.form.get('osmo')),
            cond = int(request.form.get('cond')),
            urea = int(request.form.get('urea')),
            calc = int(request.form.get('calc'))
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