# filename: stock_plot_script.py
from functions import get_stock_prices, plot_stock_prices

# Define the stock symbols and the date range
stock_symbols = ['NVDA', 'TSLA']
start_date = '2024-01-01'
end_date = '2024-05-30'

# Get the stock prices
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Plot the stock prices and save it to a file
plot_stock_prices(stock_prices, 'stock_prices_YTD_plot.png')