from project import FormulaTeam


class RedBullTeam(FormulaTeam):

    def team_data(self):
        expenses = 250_000
        sponsors = {"Oracle": {1: 1_500_000, 2: 800_000},
                    "Honda": {8: 20_000, 10: 10_000}}
        return expenses, sponsors


    def calculate_revenue_after_race(self, race_pos):
        pass
