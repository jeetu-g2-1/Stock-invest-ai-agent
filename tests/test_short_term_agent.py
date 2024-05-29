import unittest
from agents.short_term_agent import ShortTermAgent

class TestShortTermAgent(unittest.TestCase):

    def test_recommendation(self):
        # Create an instance of the ShortTermAgent
        agent = ShortTermAgent()

        # Call the recommend method
        recommendation = agent.recommend()

        # Assert that the recommendation is not empty
        self.assertTrue(recommendation)

if __name__ == '__main__':
    unittest.main()

