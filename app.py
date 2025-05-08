# app.py
from flask import Flask, render_template, request
from utils.data_preprocessing import preprocess_data
from model.lstm_model import predict_stock
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file:
        return "No file uploaded"

    df = pd.read_csv(file)
    processed_data, scaler = preprocess_data(df)
    predictions = predict_stock(processed_data, scaler)

    return render_template('index.html', predictions=predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
