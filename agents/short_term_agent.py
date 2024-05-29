from utils import clean_value

class ShortTermAgent:
    def __init__(self, name="ShortTermAgent"):
        self.name = name

    def recommend(self, amount, companies_data):
        recommendations = {}
        for company in companies_data:
            # Example heuristic for short-term: focus on recent price changes
            recent_change = clean_value(company.get('50DayMovingAverage')) - clean_value(company.get('200DayMovingAverage'))
            recommendations[company['Symbol']] = recent_change

        total_score = sum(recommendations.values())
        for company in recommendations:
            recommendations[company] = (recommendations[company] / total_score) * amount

        return recommendations
