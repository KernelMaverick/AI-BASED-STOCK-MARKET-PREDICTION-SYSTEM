
# AI-Based Stock Market Prediction System

This project uses machine learning to predict stock market trends based on historical data. It uses an LSTM model for time series forecasting and displays predictions through a Flask web interface.

## 🔧 Technologies Used
- Python
- Scikit-learn
- TensorFlow (LSTM)
- Pandas, NumPy
- Matplotlib
- Flask
- HTML/CSS

## 📈 Features
- LSTM-based stock price forecasting
- Clean and interactive UI with Flask
- Graphical visualization of historical vs predicted data
- CSV file upload support for custom datasets

## 🚀 Getting Started
1. Clone the repository:
```

git clone [https://github.com/yourusername/ai-stock-market-predictor.git](https://github.com/kernelmaverick/ai-stock-market-predictor.git)

```
2. Install dependencies:
```

pip install -r requirements.txt

```
3. Run the Flask app:
```

python app.py

```

4. Open `http://127.0.0.1:5000/` in your browser.

## 📂 Folder Structure


ai-stock-market-predictor/
├── app.py
├── model/
│   └── lstm\_model.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── utils/
│   └── data\_preprocessing.py
├── sample\_data/
│   └── stock\_prices.csv
├── requirements.txt
└── README.md



## 📄 License
This project is open-source and available under the [MIT License](LICENSE).


 📄 `requirements.txt`


flask
numpy
pandas
scikit-learn
matplotlib
tensorfl
