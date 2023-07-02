from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):


    def calculate_revenue_after_race(self, race_pos: int):
        sponsors_Oracle = {
            1: 1500000,
            2: 800000
        }
        sponsors_Honda = {
            8: 20000,
            10: 10000
        }
        expenses = 250000

        result = 0

        for k, v in sponsors_Honda.items():
            if race_pos <= k:
                result += v
                break

        for k, v in sponsors_Oracle.items():
            if race_pos <= k:
                result += v
                break

        self.budget += result - expenses

        return f"The revenue after the race is {result - expenses}$. Current budget {self.budget}$"

