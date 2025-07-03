class Game:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def get_info(self):
        return f"{self.name} ({self.genre})"
