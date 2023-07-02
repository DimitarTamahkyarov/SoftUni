from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors_Petronas = {
            1: 1000000,
            3: 500000
        }
        sponsors_TeamViewer = {
            5: 100000,
            7: 50000
        }
        expenses = 200000

        result = 0

        for k, v in sponsors_Petronas.items():
            if race_pos <= k:
                result += v
                break

        for k, v in sponsors_TeamViewer.items():
            if race_pos <= k:
                result += v
                break

        self.budget += result - expenses

        return f"The revenue after the race is {result - expenses}$. Current budget {self.budget}$"