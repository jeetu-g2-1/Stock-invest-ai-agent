import unittest
from unittest.mock import patch
from input_handler import validate_user_input, get_valid_input

class TestInputHandler(unittest.TestCase):

    @patch('builtins.input', side_effect=['low'])
    def test_validate_user_input_valid(self, mock_input):
        # Call the function under test
        validated_input = validate_user_input('risk_tolerance', ['low', 'moderate', 'high'])

        # Assert that the input function was called once
        mock_input.assert_called_once()

        # Assert that the validated input matches the expected value
        self.assertEqual(validated_input, 'low')

    @patch('builtins.input', side_effect=['invalid', 'low'])
    def test_validate_user_input_invalid_then_valid(self, mock_input):
        # Call the function under test
        validated_input = validate_user_input('risk_tolerance', ['low', 'moderate', 'high'])

        # Assert that the input function was called twice
        self.assertEqual(mock_input.call_count, 2)

        # Assert that the validated input matches the second valid input
        self.assertEqual(validated_input, 'low')

    @patch('builtins.input', side_effect=['invalid', 'invalid', 'low'])
    def test_get_valid_input(self, mock_input):
        # Call the function under test
        validated_input = get_valid_input('risk_tolerance', ['low', 'moderate', 'high'])

        # Assert that the input function was called three times
        self.assertEqual(mock_input.call_count, 3)

        # Assert that the validated input matches the valid input provided
        self.assertEqual(validated_input, 'low')

if __name__ == '__main__':
    unittest.main()

