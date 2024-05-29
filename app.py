from uagents import Agent, Context
from api_data_collector import get_company_data
from agents.long_term_agent import LongTermAgent
from agents.short_term_agent import ShortTermAgent
from agents.low_risk_agent import LowRiskAgent

# List of long-term investment companies
long_term_companies = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "JNJ", "PG", "KO", "PEP", "V", "NVDA",
    "JPM", "DIS", "HD", "BRK.B", "INTC", "MCD", "PFE", "CSCO", "VZ", "CVX"
]

# List of short-term investment companies
short_term_companies = [
    "TSLA", "AMD", "ZM", "ROKU", "SQ", "MRNA", "PTON", "BYND", "SNOW", "SHOP", "ABNB"
]

# Initialize the agents
long_term_agent = Agent(name="LongTermAgent", seed="long_term_agent_seed")
short_term_agent = Agent(name="ShortTermAgent", seed="short_term_agent_seed")
low_risk_agent = Agent(name="LowRiskAgent", seed="low_risk_agent_seed")

@long_term_agent.on_interval(period=10.0)
async def recommend_long_term(ctx: Context):
    ctx.logger.info(f'Long-term agent is evaluating companies...')
    user_profile = {
        'risk_tolerance': 'moderate',
        'investment_goals': 'long_term_growth',
        'total_investment': 10000
    }
    company_data = [get_company_data(symbol) for symbol in long_term_companies]

    agent = LongTermAgent()
    recommendations = agent.recommend(user_profile['total_investment'], company_data)

    for company, amount in recommendations.items():
        ctx.logger.info(f"Invest ${amount:.2f} in {company}")

@short_term_agent.on_interval(period=15.0)
async def recommend_short_term(ctx: Context):
    ctx.logger.info(f'Short-term agent is evaluating companies...')
    user_profile = {
        'risk_tolerance': 'moderate',
        'investment_goals': 'short_term_gains',
        'total_investment': 5000
    }
    company_data = [get_company_data(symbol) for symbol in short_term_companies]

    agent = ShortTermAgent()
    recommendations = agent.recommend(user_profile['total_investment'], company_data)

    for company, amount in recommendations.items():
        ctx.logger.info(f"Invest ${amount:.2f} in {company}")

@low_risk_agent.on_interval(period=20.0)
async def recommend_low_risk(ctx: Context):
    ctx.logger.info(f'Low-risk agent is evaluating companies...')
    user_profile = {
        'risk_tolerance': 'low',
        'investment_goals': 'capital_preservation',
        'total_investment': 8000
    }
    # Use long-term companies for low-risk evaluation for simplicity
    company_data = [get_company_data(symbol) for symbol in long_term_companies]

    agent = LowRiskAgent()
    recommendations = agent.recommend(user_profile['total_investment'], company_data)

    for company, amount in recommendations.items():
        ctx.logger.info(f"Invest ${amount:.2f} in {company}")

if __name__ == "__main__":
    long_term_agent.run()
    short_term_agent.run()
    low_risk_agent.run()

