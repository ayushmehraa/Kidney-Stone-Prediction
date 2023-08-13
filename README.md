<div align="center">
    <h1 align="center">
        <img width="80" height="80" src="https://img.icons8.com/officel/80/kidney.png" alt="kidney"/>
        <br>Student Performance Indicator Prediction
    </h1>
</div>
<h3 align="center">
Predict student performance based by using data and A.I
</h3>
<br>
<h3 align="center">
Technologies used.
</h3>
<br>
<p align="center">
        <img width="48" height="48" src="https://img.icons8.com/fluency/48/python.png" alt="python"/>
        <img width="48" height="48" src="https://img.icons8.com/fluency/48/jupyter.png" alt="jupyter"/>
        <img width="48" height="48" src="https://img.icons8.com/color/48/brain-3.png" alt="brain-3"/>
        <img width="55" height="55" src="https://img.icons8.com/nolan/64/flask.png" alt="flask"/>
        <img width="48" height="48" src="https://img.icons8.com/ios-filled/50/22C3E6/html-filetype.png" alt="html-filetype"/>
        <img width="48" height="48" src="https://img.icons8.com/color/48/git.png" alt="git"/>

</p>
</div>
<br>

# 🤖 Student Performance Indicator Prediction

Welcome to the Student Performance Indicator Prediction repository! This project aims to predict student performance indicators based on various features such as gender, ethnicity, parental education, lunch type, and test preparation. The dataset used in this project is sourced from Kaggle and contains information on math, reading, and writing scores.

# 📁 Dataset

The dataset used in this project can be downloaded from the following link:
[Student Performance Indicator dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)

- gender: Sex of the student (Male/Female).
- race/ethnicity: Ethnicity of the student (Group A, B, C, D, E).
- parental level of education: Parents' final education (Bachelor's degree, Some college, Master's degree, Associate's degree, High school).
- lunch: Type of lunch before the test (Standard or Free/Reduced).
- test preparation course: Completion status of the test = preparation course (Complete or Not Complete).
- math score: Score obtained in the math test.
- reading score: Score obtained in the reading test.
- writing score: Score obtained in the writing test.


# ⚒️ Project Structure
The project is organized as follows:

- artifacts: This directory contains important artifacts such as data, preprocessor, and model pickle files.
- notebooks: Jupyter notebooks for data exploration and model training.
- src: Source code for the project.
- components: Contains Python files for data ingestion, transformation, and modeling.
- pipeline: Houses the predict_pipeline.py file with prediction methods.
- static: Images used in the Flask app template.
- templates: HTML files for the Flask app.
- app.py: Flask web application for student performance prediction.
- requirements.txt: List of required dependencies.
- setup.py: Setup script for the project.

# 🚀 Getting Started

1. Clone this repository to your local machine using:
```
git clone https://github.com/yourusername/student-performance-prediction.git

```

- Install the required dependencies using:

```
pip install -r requirements.txt
```

- Download the dataset (student_performance_dataset.csv) from the provided Kaggle link and place it inside the artifacts/data directory.

- Run the web application using:
```
python app.py

```
- Access the web app by navigating to http://localhost:5000 in your web browser.

# 📋 Results
The web application provides users with an interface to input student information and receive predictions regarding their performance indicators. The underlying model's performance can be further analyzed using the Jupyter notebooks in the notebooks directory.

# 🤝 Contributors
Feel free to contribute to this project by creating pull requests, reporting issues, or suggesting improvements. Your contributions are greatly appreciated!

# 💳License
This project is licensed under the MIT License.

