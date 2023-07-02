import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

api_key = 'RW9XVB8H9ZFI4CCX'  # Replace with your actual API key
symbol = 'AAPL'  # Replace with the stock symbol you want to analyze

# url = f'https://api.example.com/endpoint?symbol={symbol}&apikey={api_key}'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}'

response = requests.get(url)
data = response.json()
# print(data)

df = pd.DataFrame(data)  # Assuming the data is in JSON format
# Perform data analysis and calculations

# Plot a simple line graph
# plt.plot(df['date'], df['close'])
# plt.xlabel('Date')
# plt.ylabel('Closing Price')
# plt.title('Stock Market Analysis')
# plt.show()

# Extract 'date' and 'close' values from the data
time_series = data['Time Series (5min)']
df = pd.DataFrame(time_series).T
df.index = pd.to_datetime(df.index)
df['close'] = df['4. close'].astype(float)

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['close'])
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Price Analysis')
plt.grid(True)
plt.show()
