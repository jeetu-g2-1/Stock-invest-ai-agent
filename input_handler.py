# input.py

def get_user_profile():
    # Function to get user profile data
    # Example implementation:
    user_profile = {}
    user_profile['risk_tolerance'] = input("Enter your risk tolerance (low/moderate/high): ")
    user_profile['investment_goals'] = input("Enter your investment goals (long_term_growth/short_term_gains/low_risk): ")
    user_profile['total_investment'] = float(input("Enter your total investment amount: "))
    return user_profile

