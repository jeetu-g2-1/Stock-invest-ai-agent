import pandas as pd
import numpy as np

def calculate_rolling_average(data, window_size=30):
    """
    Calculate the rolling average of a given dataset.

    Args:
    - data: pandas DataFrame or Series containing the data to analyze
    - window_size: int, optional, default=30. The window size for the rolling average calculation.

    Returns:
    - pandas Series containing the rolling average values.
    """
    return data.rolling(window=window_size).mean()

def calculate_returns(data):
    """
    Calculate the daily returns of a given dataset.

    Args:
    - data: pandas DataFrame or Series containing the data to analyze

    Returns:
    - pandas Series containing the daily returns.
    """
    return data.pct_change().fillna(0)

def calculate_volatility(data, window_size=30):
    """
    Calculate the volatility of a given dataset.

    Args:
    - data: pandas DataFrame or Series containing the data to analyze
    - window_size: int, optional, default=30. The window size for the volatility calculation.

    Returns:
    - pandas Series containing the volatility values.
    """
    return data.pct_change().rolling(window=window_size).std()

def analyze_stock_data(stock_data):
    """
    Perform various data analysis on stock data.

    Args:
    - stock_data: pandas DataFrame containing stock data (e.g., Open, High, Low, Close prices).

    Returns:
    - Dictionary containing the analysis results.
    """
    analysis_results = {}

    # Calculate rolling average
    analysis_results['rolling_average'] = calculate_rolling_average(stock_data['Close'])

    # Calculate daily returns
    analysis_results['daily_returns'] = calculate_returns(stock_data['Close'])

    # Calculate volatility
    analysis_results['volatility'] = calculate_volatility(stock_data['Close'])

    return analysis_results

