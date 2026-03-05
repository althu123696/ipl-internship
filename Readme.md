# 🏏 IPL Auction Prediction Project


## overview

This project demonstrates an end-to-end machine learning workflow for predicting IPL Runs of players.  
It includes:
- Scrapping
- Data preprocessing and feature engineering  
- Regression models (Linear, Polynomial, Decision Tree, KNN, Gradient Boosting)  
- Hyperparameter tuning gridsearchCV 
- Model deployment with Streamlit  

---

## project structure

IPL_PROJECT/
│── data/
│   └── ipl_auction.csv              # Dataset
│
│── notebooks/
│   └── ipl.ipynb                    # End-to-end notebook
│
│── models/
│   └── poly_linear_regression_pipeline.pkl   # Saved trained model
│
│── app/
│   └── streamlit_app.py             # Streamlit app for predictions
│
│── requirements.txt                  # Dependencies
│── README.md                         # Project overview



---

##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Althu123696/ipl_internship_
cd < ipl_internship >


## Install Dependencies

pip install -r requirements.txt


## Requirements

Dependencies are listed in requirements.txt:
requests
beautifulsoup4
pandas
selenium
matplotlib
seaborn
scikit-learn
streamlit
optuna
mlflow


## Running jupiter notebook

To explore the workflow:
1. Activate your virtual environment.
2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook

## 🎛 Running the Streamlit App

To interact with the trained model through a web interface:

1. Activate your virtual environment:
   ```bash
   venv\Scripts\activate   # Windows
  
2. Launch streamlit app 
streamlit run app/streamlit_app.py
dockerize all