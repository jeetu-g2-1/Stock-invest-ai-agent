from utils import heuristic_score

class LongTermAgent:
    def __init__(self, name="LongTermAgent"):
        self.name = name

    def recommend(self, amount, companies_data):
        recommendations = {}
        for company in companies_data:
            score = heuristic_score(company)
            recommendations[company['Symbol']] = score

        total_score = sum(recommendations.values())
        for company in recommendations:
            recommendations[company] = (recommendations[company] / total_score) * amount

        return recommendations
