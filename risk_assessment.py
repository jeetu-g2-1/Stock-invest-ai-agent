def assess_risk_tolerance(risk_profile):
    """
    Assess the risk tolerance based on the user's risk profile.

    Args:
    - risk_profile: dict. User's risk profile containing risk tolerance information.

    Returns:
    - Risk assessment result (e.g., low, moderate, high).
    """
    risk_tolerance = risk_profile.get('risk_tolerance')
    if risk_tolerance == 'low':
        return 'low'
    elif risk_tolerance == 'moderate':
        return 'moderate'
    elif risk_tolerance == 'high':
        return 'high'
    else:
        return 'unknown'

def assess_investment_risk(company_data):
    """
    Assess the investment risk of companies based on their financial data.

    Args:
    - company_data: list of dict. Financial data of companies.

    Returns:
    - Dictionary mapping company names to risk assessment results.
    """
    risk_assessment_results = {}
    for company in company_data:
        # Example risk assessment logic based on financial data
        if company.get('PE_ratio') < 15:
            risk_assessment_results[company['name']] = 'low risk'
        elif company.get('PE_ratio') < 30:
            risk_assessment_results[company['name']] = 'moderate risk'
        else:
            risk_assessment_results[company['name']] = 'high risk'
    return risk_assessment_results

