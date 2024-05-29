
import unittest
import pandas as pd
import numpy as np
from your_module_name import calculate_rolling_average, calculate_returns, calculate_volatility, analyze_stock_data

class TestStockAnalysis(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
        data = {
            'Open': np.random.rand(100),
            'High': np.random.rand(100),
            'Low': np.random.rand(100),
            'Close': np.random.rand(100)
        }
        self.stock_data = pd.DataFrame(data, index=dates)

    def test_calculate_rolling_average(self):
        rolling_average = calculate_rolling_average(self.stock_data['Close'], window_size=30)
        # Check if rolling average is a pandas Series
        self.assertIsInstance(rolling_average, pd.Series)
        # Check if rolling average has the correct length
        self.assertEqual(len(rolling_average), 100)

    def test_calculate_returns(self):
        returns = calculate_returns(self.stock_data['Close'])
        # Check if returns is a pandas Series
        self.assertIsInstance(returns, pd.Series)
        # Check if returns has the correct length
        self.assertEqual(len(returns), 100)
        # Check if the first return is zero
        self.assertEqual(returns.iloc[0], 0)

    def test_calculate_volatility(self):
        volatility = calculate_volatility(self.stock_data['Close'], window_size=30)
        # Check if volatility is a pandas Series
        self.assertIsInstance(volatility, pd.Series)
        # Check if volatility has the correct length
        self.assertEqual(len(volatility), 100)

    def test_analyze_stock_data(self):
        analysis_results = analyze_stock_data(self.stock_data)
        # Check if analysis results is a dictionary
        self.assertIsInstance(analysis_results, dict)
        # Check if keys in the dictionary are as expected
        self.assertIn('rolling_average', analysis_results)
        self.assertIn('daily_returns', analysis_results)
        self.assertIn('volatility', analysis_results)
        # Check if values are pandas Series
        self.assertIsInstance(analysis_results['rolling_average'], pd.Series)
        self.assertIsInstance(analysis_results['daily_returns'], pd.Series)
        self.assertIsInstance(analysis_results['volatility'], pd.Series)

if __name__ == '__main__':
    unittest.main()
