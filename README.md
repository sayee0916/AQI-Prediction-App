🌍 Air Quality Index Prediction Using Machine Learning
Overview

Air pollution has become one of the most serious environmental issues worldwide, affecting human health, ecosystems, and climate. The Air Quality Index (AQI) is a standardized indicator used to measure and communicate the level of air pollution in a particular area.

This project develops a Machine Learning-based AQI Prediction System that estimates air quality levels based on major air pollutants.

The model predicts AQI using pollutant concentration values such as:

• PM2.5 – Fine particulate matter
• PM10 – Coarse particulate matter
• NO₂ – Nitrogen Dioxide
• SO₂ – Sulfur Dioxide
• CO – Carbon Monoxide
• O₃ – Ozone

A Streamlit web application is deployed to allow users to input pollutant values and instantly predict the AQI level.

Problem Statement

Air pollution is responsible for millions of premature deaths every year and significantly impacts public health.

Monitoring air quality in real-time and predicting AQI levels helps governments, researchers, and citizens take preventive measures.

However:

• Manual analysis of air pollution data is complex
• Air quality varies across cities and time
• Accurate prediction requires analyzing multiple pollutant factors simultaneously

Therefore, an automated machine learning system is needed to analyze pollutant levels and predict AQI efficiently and accurately.

Objectives

• Build a Machine Learning model capable of predicting AQI levels
• Analyze the impact of different pollutants on air quality
• Perform data preprocessing and cleaning for reliable predictions
• Deploy the model using Streamlit for real-time prediction
• Create an interactive interface where users can input pollutant values

Dataset

The dataset used in this project contains city-wise air pollution data from India.

Dataset Features
Feature	Description
PM2.5	Fine particulate matter concentration
PM10	Coarse particulate matter concentration
NO₂	Nitrogen dioxide level
SO₂	Sulfur dioxide level
CO	Carbon monoxide concentration
O₃	Ozone concentration
City	Location of monitoring station
AQI	Target variable representing air quality

The dataset was cleaned and preprocessed before training the model.

Data Preprocessing

The following steps were performed before training the model:

• Handling missing values
• Removing inconsistent records
• Feature selection
• Encoding categorical variables (City)
• Data normalization

These steps ensure that the machine learning model learns meaningful patterns from the dataset.

Machine Learning Model

A Regression-based Machine Learning model was trained to predict AQI values.

Model Workflow

1️⃣ Data preprocessing
2️⃣ Feature selection
3️⃣ Model training
4️⃣ Model evaluation
5️⃣ Model deployment

The trained model is saved as:

aqi_model.pkl

The feature structure is stored in:

columns.pkl
AQI Classification Scale

The predicted AQI values fall into different categories based on pollution severity.

AQI Range	Category
0 – 50	Good
51 – 100	Moderate
101 – 150	Unhealthy for Sensitive Groups
151 – 200	Unhealthy
201 – 300	Very Unhealthy
301 – 500	Hazardous

These categories help interpret the AQI value in terms of health impact.

Web Application (Streamlit)

A Streamlit web application is developed to make AQI prediction interactive.

Application Features

• User-friendly interface
• Input pollutant values easily
• Select city from dropdown
• Instant AQI prediction
• Visual AQI gauge representation

Users can quickly evaluate air quality levels by entering pollutant concentrations.

Project Structure
AQI_Prediction
│
├── app.py
├── aqi_model.pkl
├── columns.pkl
├── requirements.txt
└── README.md
Deployment

The project is deployed using Streamlit Cloud.

Users can access the web application online and predict AQI values in real time.

Technologies Used
Technology	Purpose
Python	Programming language
Pandas	Data processing
NumPy	Numerical operations
Scikit-learn	Machine learning model
Streamlit	Web application
Plotly	Data visualization
Applications

This system can be useful for:

• Environmental monitoring
• Smart city planning
• Pollution awareness systems
• Public health monitoring
• Government environmental agencies

Future Improvements

• Integration with real-time air quality APIs
• Time-series forecasting of AQI trends
• Mobile application for AQI monitoring
• Geographic AQI visualization on maps

Author

Sayali Sanjay Chidrawar

B.Tech Computer Science Graduate (2025)
Interested in Data Analytics, Machine Learning, and Data Visualization.
