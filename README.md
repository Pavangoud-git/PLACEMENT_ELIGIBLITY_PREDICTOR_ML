🎓 Placement Eligibility Predictor

A Machine Learning-based Placement Eligibility Predictor that predicts whether a student is eligible for campus placement based on academic and performance factors such as CGPA, Aptitude Score, and Attendance.



This project demonstrates a complete beginner-friendly machine learning workflow, from data preprocessing and model training to evaluation and deployment using Streamlit.

🚀 Project Overview

The Placement Eligibility Predictor uses Logistic Regression to classify students into two categories:



 ✅ Eligible for Placement 

 ❌ Not Eligible for Placement 

Example



CGPA: 8.2
Aptitude Score: 78
Attendance: 85%

Prediction:
✅ Eligible for Placement

The model learns patterns from historical student data and uses them to predict the placement eligibility of new students.

✨ Features

 📊 Student placement prediction 

 🧹 Data cleaning and preprocessing 

 🔍 Exploratory Data Analysis (EDA) 

 🎯 Feature and target separation 

 ✂️ Train-Test Split 

 📏 Feature Scaling 

 🤖 Logistic Regression 

 📈 Model Evaluation 

 💾 Save trained model 

 🖥️ Interactive Streamlit application 

 🚀 Deployment-ready project 

🛠️ Technologies Used

Technology

Purpose

Python

Core programming language

Pandas

Data manipulation

NumPy

Numerical operations

Matplotlib

Data visualization

Seaborn

Exploratory Data Analysis

Scikit-learn

Machine Learning

Streamlit

Web application

Joblib / Pickle

Model saving

Git & GitHub

Version control

🧠 Machine Learning Workflow



Student Dataset
      ↓
Data Understanding
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature / Target Separation
      ↓
Train-Test Split
      ↓
Feature Scaling
      ↓
Logistic Regression
      ↓
Model Evaluation
      ↓
Save Model
      ↓
Streamlit Application
      ↓
Deployment

📂 Dataset

The dataset contains student-related information used to predict placement eligibility.

Features

Feature

Description

CGPA

Student's academic performance

Aptitude_Score

Student's aptitude test score

Attendance

Student's attendance percentage

Placement_Eligible

Target variable

Target Variable



Placement_Eligible

Typical values:



1 → Eligible
0 → Not Eligible

🔎 Exploratory Data Analysis

EDA is used to understand the dataset and identify relationships between student performance and placement eligibility.



The analysis includes:



 CGPA distribution 

 Aptitude Score distribution 

 Attendance distribution 

 Eligible vs. non-eligible students 

 Feature relationships 

 Correlation analysis 

🤖 Machine Learning Model

Logistic Regression

Logistic Regression is used as the primary classification algorithm because placement eligibility is a binary classification problem.



Eligible
    vs
Not Eligible

The model predicts the probability that a student belongs to the eligible class.

📏 Feature Scaling

Since the input features have different numerical ranges, StandardScaler is used to scale the features before training the Logistic Regression model.



CGPA
Aptitude Score
Attendance
      ↓
StandardScaler
      ↓
Scaled Features
      ↓
Logistic Regression

📊 Model Evaluation

The model can be evaluated using:



 Accuracy 

 Precision 

 Recall 

 F1-Score 

 Confusion Matrix 

 Classification Report 



Example:



Accuracy  : XX%
Precision : XX%
Recall    : XX%
F1-Score  : XX%

Replace XX% with your actual model results.

🖥️ Streamlit Application

The project includes an interactive web application where users can enter student information.

Input



CGPA
Aptitude Score
Attendance

Output



✅ Eligible for Placement

or



❌ Not Eligible for Placement

📁 Project Structure



Placement_Eligibility_Predictor/
│
├── dataset.csv
├── Placement_Eligibility_Predictor.ipynb
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── screenshots/
    └── app.png

Change the filenames above according to your actual GitHub project files.

⚙️ Installation

1. Clone the repository



git clone https://github.com/your-username/Placement_Eligibility_Predictor.git

2. Open the project folder



cd Placement_Eligibility_Predictor

3. Install required libraries



pip install -r requirements.txt

▶️ Run the Application

Run the Streamlit application using:



streamlit run app.py

The application will open in your web browser.

📦 Requirements

Example requirements.txt:



pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
joblib

🧪 Example Prediction

Input



CGPA = 8.2
Aptitude Score = 78
Attendance = 85

Output



✅ Eligible for Placement

The actual prediction depends on the trained model and dataset.

🎯 Project Objectives

The main objectives of this project are:



 Understand student placement data. 

 Analyze factors related to placement eligibility. 

 Build a machine learning classification model. 

 Evaluate model performance. 

 Save the trained model. 

 Create an interactive prediction application. 

 Deploy the machine learning solution. 

📚 Concepts Demonstrated

 Data Cleaning 

 Exploratory Data Analysis 

 Feature Engineering 

 Classification 

 Logistic Regression 

 Train-Test Split 

 Feature Scaling 

 Model Evaluation 

 Model Persistence 

 Streamlit 

 Machine Learning Deployment 

🔮 Future Enhancements

 Add Random Forest and XGBoost 

 Compare multiple ML algorithms 

 Add more student features 

 Display prediction probability 

 Use a larger real-world dataset 

 Add SHAP model explainability 

 Add placement analytics dashboard 

 Deploy on Streamlit Community Cloud 

🌐 Deployment

This project can be deployed using Streamlit Community Cloud.



Make sure your GitHub repository contains:



app.py
requirements.txt
model files

Then connect the repository to Streamlit Community Cloud and select app.py as the main application file.

👨‍💻 Author

Bheemagani Pavan



Aspiring Data Analyst | Data Scientist | Machine Learning Enthusiast



GitHub: https://github.com/Pavangoud-git



LinkedIn: https://linkedin.com/in/pavan-bheemagani-632b4732b2

⭐ Project Highlight

An end-to-end machine learning project that predicts student placement eligibility and integrates the trained classification model into an interactive Streamlit web application.

⭐ If you find this project useful, consider giving the repository a star!
