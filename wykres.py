import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical stock data for Amazon
amazon_stock = yf.download('AMZN', start='2015-01-01', end='2023-01-01')

# Plotting Amazon stocks in red
plt.figure(figsize=(10, 6))
plt.plot(amazon_stock['Close'], color='green', label='Amazon Stock (AMZN)')
plt.title('Amazon Stock Prices')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()

# Calculate and print the maximum stock value
max_stock_value = amazon_stock['Close'].max()
print(f'Maximum Stock Value: ${max_stock_value:.2f}')

# Show the plot
plt.show()

