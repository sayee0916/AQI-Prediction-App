🌍 Air Quality Index Prediction Using Machine Learning

📌 Overview

Air pollution is one of the most serious environmental challenges affecting human health and ecosystems worldwide. The Air Quality Index (AQI) is a standardized metric used to measure and communicate air pollution levels in a particular region.

This project develops a Machine Learning-based AQI Prediction System that estimates air quality based on major pollutant concentrations.

The system analyzes key pollutants including:

PM2.5 – Fine particulate matter

PM10 – Coarse particulate matter

NO₂ – Nitrogen Dioxide

SO₂ – Sulfur Dioxide

CO – Carbon Monoxide

O₃ – Ozone

A Streamlit web application allows users to input pollutant values and instantly predict AQI levels.

⚠️ Problem Statement

Air pollution causes millions of premature deaths each year and has severe health impacts on respiratory and cardiovascular systems.

However:

Air quality varies significantly across cities and time

Multiple pollutants contribute to AQI simultaneously

Manual monitoring and prediction is complex

Therefore, an automated machine learning system is required to analyze pollution data and predict AQI efficiently.

🎯 Objectives

The main objectives of this project are:

Develop a Machine Learning model capable of predicting AQI

Analyze the impact of different pollutants on air quality

Perform data preprocessing and cleaning for accurate predictions

Build an interactive web application using Streamlit

Enable real-time AQI prediction based on pollutant inputs

📊 Dataset

The dataset contains city-wise air pollution measurements from India.

| Feature | Description                              |
| ------- | ---------------------------------------- |
| PM2.5   | Fine particulate matter concentration    |
| PM10    | Coarse particulate matter concentration  |
| NO₂     | Nitrogen dioxide level                   |
| SO₂     | Sulfur dioxide level                     |
| CO      | Carbon monoxide concentration            |
| O₃      | Ozone concentration                      |
| City    | Monitoring station location              |
| AQI     | Target variable representing air quality |


The dataset was cleaned and processed before training the model.

🧹 Data Preprocessing

Before training the model, several preprocessing steps were performed:

Handling missing values

Removing inconsistent or invalid records

Feature selection

Encoding categorical variables (City)

Preparing data for machine learning models

These steps improve the accuracy and reliability of the prediction model.

🤖 Machine Learning Model

A Regression-based Machine Learning model was trained to predict AQI values based on pollutant concentrations.

Model Workflow

Data preprocessing

Feature selection

Model training

Model evaluation

Model deployment

🌈 AQI Classification Scale

AQI values are categorized based on pollution severity:

| AQI Range | Category                       |
| --------- | ------------------------------ |
| 0 – 50    | Good                           |
| 51 – 100  | Moderate                       |
| 101 – 150 | Unhealthy for Sensitive Groups |
| 151 – 200 | Unhealthy                      |
| 201 – 300 | Very Unhealthy                 |
| 301 – 500 | Hazardous                      |


These categories help interpret AQI levels in terms of health impact.

💻 Web Application (Streamlit)

A Streamlit web application was developed to allow users to interact with the model.

Features

User-friendly interface

Input pollutant values easily

Select city from dropdown

Instant AQI prediction

Interactive AQI visualization

Users can quickly evaluate air quality conditions using the web application.

📂 Project Structure
AQI_Prediction
│
├── app.py
├── aqi_model.pkl
├── columns.pkl
├── requirements.txt
└── README.md
🚀 Deployment

The application is deployed using Streamlit Cloud, allowing users to access the AQI prediction system online.

Users can enter pollutant levels and receive instant AQI predictions through the deployed web interface.

🛠 Technologies Used
Technology	Purpose
Python	Programming language
Pandas	Data analysis and preprocessing
NumPy	Numerical computations
Scikit-learn	Machine learning model
Streamlit	Web application framework
Plotly	Data visualization

🌍 Applications

This system can be used for:

Environmental monitoring systems

Smart city pollution analysis

Public health awareness tools

Government environmental agencies

Pollution research and analysis

🔮 Future Improvements

Possible future enhancements include:

Integration with real-time air quality APIs

Time-series AQI forecasting

Mobile application for AQI monitoring

Interactive AQI maps for different cities

👩‍💻 Author

Sayali Sanjay Chidrawar
