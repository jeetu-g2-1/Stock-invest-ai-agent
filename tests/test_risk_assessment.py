import unittest
from risk_assessment import assess_risk_tolerance, assess_investment_risk

class TestRiskAssessment(unittest.TestCase):

    def test_assess_risk_tolerance(self):
        # Test low risk tolerance
        low_risk_profile = {'risk_tolerance': 'low'}
        self.assertEqual(assess_risk_tolerance(low_risk_profile), 'low')

        # Test moderate risk tolerance
        moderate_risk_profile = {'risk_tolerance': 'moderate'}
        self.assertEqual(assess_risk_tolerance(moderate_risk_profile), 'moderate')

        # Test high risk tolerance
        high_risk_profile = {'risk_tolerance': 'high'}
        self.assertEqual(assess_risk_tolerance(high_risk_profile), 'high')

        # Test unknown risk tolerance
        unknown_risk_profile = {'risk_tolerance': 'unknown'}
        self.assertEqual(assess_risk_tolerance(unknown_risk_profile), 'unknown')

    def test_assess_investment_risk(self):
        # Example financial data for testing
        company_data = [
            {'name': 'Company A', 'PE_ratio': 10},
            {'name': 'Company B', 'PE_ratio': 25},
            {'name': 'Company C', 'PE_ratio': 35}
        ]

        # Test risk assessment for company A
        risk_assessment_results = assess_investment_risk(company_data)
        self.assertEqual(risk_assessment_results['Company A'], 'low risk')

        # Test risk assessment for company B
        self.assertEqual(risk_assessment_results['Company B'], 'moderate risk')

        # Test risk assessment for company C
        self.assertEqual(risk_assessment_results['Company C'], 'high risk')

if __name__ == '__main__':
    unittest.main()

