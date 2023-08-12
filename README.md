<div align="center">
    <h1 align="center">
        <img width="80" height="80" src="https://img.icons8.com/officel/80/kidney.png" alt="kidney"/>
        <br>Kidney Stone Prediction
    </h1>
</div>
<h3 align="center">
Predict Risk of Stone in your kidney with data and AI and plan keep safe.
</h3>
<br>
<h3 align="center">
Technologies used.
</h3>
<br>
<p align="center">
        <img width="48" height="48" src="https://img.icons8.com/fluency/48/python.png" alt="python"/>
        <img width="48" height="48" src="https://img.icons8.com/fluency/48/jupyter.png" alt="jupyter"/>
        <img width="48" height="48" src="https://img.icons8.com/dotty/80/228BE6/visible.png" alt="visible"/>
        <img width="48" height="48" src="https://img.icons8.com/color/48/brain-3.png" alt="brain-3"/>
        <img width="55" height="55" src="https://img.icons8.com/nolan/64/flask.png" alt="flask"/>
        <img width="48" height="48" src="https://img.icons8.com/ios-filled/50/22C3E6/html-filetype.png" alt="html-filetype"/>
        <img width="48" height="48" src="https://img.icons8.com/color/48/git.png" alt="git"/>

</p>
</div>
<br>

# 🤖 Kidney Stone Prediction

This repository contains the code and resources for a machine learning project focused on predicting the likelihood of kidney stone formation based on urine analysis data. The dataset used in this project is the Kidney Stone Prediction based on Urine Analysis dataset sourced from Kaggle. The goal of this project is to develop a predictive model that can assist in identifying individuals who are at a higher risk of developing kidney stones based on their urine composition.

# 📁 Dataset

The dataset used in this project can be downloaded from the following link:
[Kidney Stone Prediction based on Urine Analysis Dataset](https://www.kaggle.com/competitions/playground-series-s3e12/data)

- Age: Age of the patient.
- Gender: Gender of the patient (Male/Female).
- CalciumOxalate: Level of calcium oxalate in urine.
- UricAcid: Level of uric acid in urine.
- CalciumPhosphate: Level of calcium phosphate in urine.
- MagnesiumAmmoniumPhosphate: Level of magnesium ammonium phosphate in urine.
- UrinepH: pH level of urine.
- SpecificGravity: Specific gravity of urine.
- KidneyStone: Target variable (0: No kidney stone, 1: Kidney stone present).


# ⚒️ Project Structure
The project is organized as follows:

- data: This directory contains the dataset file (kidney_stone_dataset.csv).
- static: This directory holds images and visual resources used in this templates.
- notebooks: Jupyter notebooks used for data exploration, preprocessing, model training, and evaluation.
- artifacts: contaions data, preprocessor and model pickle files.
- src: Source code for the project.
EDA_Kidney stone.ipynb: Data exploration and preprocessing utilities.
- model_training.ipypy: notebook for training machine learning models.
- app.py: Flask web application for kidney stone prediction.

# 🚀 Getting Started

- Clone this repository to your local machine using:
```
git clone https://github.com/yourusername/kidney-stone-prediction.git

```

- Install the required dependencies using:

```
pip install -r requirements.txt
```

- Download the dataset (kidney_stone_dataset.csv) from the provided Kaggle link and place it inside the data directory.

- Adjust the configuration in config.py as needed, including hyperparameters and file paths.

- Run the web application using:
```
python app.py

```
- Access the web app by navigating to http://localhost:5000 in your web browser.

# 📋 Results
The web application provides users with an interface to input urine analysis data and receive predictions regarding their risk of kidney stone formation. The underlying model's performance can be further fine-tuned and analyzed using the provided Jupyter notebooks in the notebooks directory.

# 🤝 Contributors
Feel free to contribute to this project by creating pull requests, reporting issues, or suggesting improvements. Your contributions are greatly appreciated!

# 💳License
This project is licensed under the MIT License.

