import pandas as pd
import random
from datetime import datetime, timedelta

# Generate sample stock price data for AAPL
date_range = pd.date_range(start='2020-01-01', end='2021-01-01', freq='B')
data = {
    'Date': date_range,
    'Open': [random.uniform(100, 200) for _ in range(len(date_range))],
    'High': [random.uniform(100, 220) for _ in range(len(date_range))],
    'Low': [random.uniform(80, 200) for _ in range(len(date_range))],
    'Close': [random.uniform(100, 210) for _ in range(len(date_range))],
    'Volume': [random.randint(1000000, 5000000) for _ in range(len(date_range))],
}

# Create DataFrame and save to CSV
df_stock = pd.DataFrame(data)
df_stock.to_csv('stock_data_aapl.csv', index=False)
