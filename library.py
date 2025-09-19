from video_game import VideoGame

class VideoGameLibrary:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def display_all_games(self):
        for game in self.games:
            game.display_info()

    def show_classics(self, current_year):
        print("Classic Games:")
        for game in self.games:
            if game.is_classic(current_year):
                print(f"- {game.title}")
