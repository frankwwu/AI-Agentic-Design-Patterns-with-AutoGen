# filename: stock_gains_ytd_plot.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_data(stock, start_date, end_date):
    return yf.download(stock, start=start_date, end=end_date)

def calculate_gains(df):
    # Normalize by the first available closing price in the year
    return df['Close']/df['Close'].iloc[0] - 1

def plot_gains(dates, gains_nvda, gains_tsla):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, gains_nvda, label='NVDA YTD Gains', marker='o')
    plt.plot(dates, gains_tsla, label='TSLA YTD Gains', marker='o')
    plt.title('YTD Stock Gains for NVDA and TSLA as of 2024-05-30')
    plt.xlabel('Date')
    plt.ylabel('Gains')
    plt.legend()
    plt.grid(True)
    plt.savefig('ytd_stock_gains.png')
    plt.show()

def main():
    start_date = '2024-01-01'
    end_date = '2024-05-30'
    data_nvda = fetch_data('NVDA', start_date, end_date)
    data_tsla = fetch_data('TSLA', start_date, end_date)

    gains_nvda = calculate_gains(data_nvda)
    gains_tsla = calculate_gains(data_tsla)

    plot_gains(data_nvda.index, gains_nvda, gains_tsla)

if __name__ == "__main__":
    main()