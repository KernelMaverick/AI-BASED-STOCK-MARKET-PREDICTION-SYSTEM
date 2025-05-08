
## model/lstm_model.py
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def build_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def predict_stock(data, scaler):
    X_train = []
    y_train = []

    for i in range(60, len(data)):
        X_train.append(data[i-60:i])
        y_train.append(data[i])

    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

    model = build_model((X_train.shape[1], 1))
    model.fit(X_train, y_train, epochs=3, batch_size=32, verbose=0)

    predictions = model.predict(X_train)
    predictions = scaler.inverse_transform(predictions)
    return predictions[-10:]
