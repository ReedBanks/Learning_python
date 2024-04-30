import pandas as pd
import random
from datetime import datetime, timedelta

# Generate sample COVID-19 data
date_range = pd.date_range(start='2020-01-01', end='2021-12-31', freq='D')
data = {
    'Date': date_range,
    'Confirmed': [random.randint(0, 1000) for _ in range(len(date_range))],
    'Deaths': [random.randint(0, 100) for _ in range(len(date_range))],
    'Recovered': [random.randint(0, 500) for _ in range(len(date_range))]
}

# Create DataFrame and save to CSV
df_covid = pd.DataFrame(data)
df_covid.to_csv('covid19_data.csv', index=False)