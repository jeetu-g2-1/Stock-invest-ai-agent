import unittest
from agents.long_term_agent import LongTermAgent

class TestLongTermAgent(unittest.TestCase):

    def test_recommendation(self):
        # Create an instance of the LongTermAgent
        agent = LongTermAgent()

        # Call the recommend method
        recommendation = agent.recommend()

        # Assert that the recommendation is not empty
        self.assertTrue(recommendation)

if __name__ == '__main__':
    unittest.main()

