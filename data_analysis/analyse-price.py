import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch stock data from Yahoo Finance
ticker = 'AAPL'  # Replace with the desired stock symbol
start_date = '2020-01-01'
end_date = '2021-01-01'
df = yf.download(ticker, start=start_date, end=end_date)

# Data analysis and visualization
df['Close'].plot(figsize=(10, 6))
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title(f'{ticker} Stock Price Analysis')
plt.show()