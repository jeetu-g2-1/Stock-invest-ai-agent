import unittest
from unittest.mock import patch
from api_data_collector import get_company_data

class TestAPIDataCollector(unittest.TestCase):

    @patch('api_data_collector.requests.get')
    def test_get_company_data_success(self, mock_requests_get):
        # Mock response from the API
        mock_response = {
            'symbol': 'AAPL',
            'name': 'Apple Inc.',
            'market_cap': '200B',
            'pe_ratio': 25
        }

        # Set up the mocked response
        mock_requests_get.return_value.json.return_value = mock_response

        # Call the function under test
        company_data = get_company_data('AAPL')

        # Assert that the API was called with the correct URL
        mock_requests_get.assert_called_once_with('https://www.alphavantage.co/query?function=OVERVIEW&symbol=AAPL&apikey=YOUR_API_KEY')

        # Assert that the returned data matches the mocked response
        self.assertEqual(company_data['symbol'], 'AAPL')
        self.assertEqual(company_data['name'], 'Apple Inc.')
        self.assertEqual(company_data['market_cap'], '200B')
        self.assertEqual(company_data['pe_ratio'], 25)

    @patch('api_data_collector.requests.get')
    def test_get_company_data_failure(self, mock_requests_get):
        # Mock a failed response from the API
        mock_requests_get.return_value.ok = False

        # Call the function under test
        company_data = get_company_data('AAPL')

        # Assert that the function returns None for failed API calls
        self.assertIsNone(company_data)

if __name__ == '__main__':
    unittest.main()

