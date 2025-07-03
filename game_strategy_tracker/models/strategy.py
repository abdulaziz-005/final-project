class SimpleStrategy:
    def __init__(self, game_name, genre, strategy_name, description, rating):
        self.game_name = game_name
        self.genre = genre
        self.strategy_name = strategy_name
        self.description = description
        self.rating = rating

    def evaluate(self):
        if self.rating >= 8:
            return "Sangat efektif"
        elif self.rating >= 5:
            return "Cukup efektif"
        else:
            return "Kurang efektif"

    def get_info(self):
        return f"{self.game_name} | {self.genre}"
