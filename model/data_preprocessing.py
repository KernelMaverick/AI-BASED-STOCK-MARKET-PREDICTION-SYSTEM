## utils/data_preprocessing.py

import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df):
    data = df['Close'].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    return scaled_data, scaler
