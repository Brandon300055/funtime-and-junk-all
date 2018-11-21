import quandl, math
import numpy as np
import pandas as pd
from sklearn.svm import SVR
import matplotlib.pyplot as plt

df = quandl.get("BCHARTS/BITSTAMPUSD", rows=500)
df = df[['Open', 'High', 'Low', 'Close', 'Volume (BTC)']]

price = df['High']

def predict_prices(prices, x):
	dates = np.reshape(date)