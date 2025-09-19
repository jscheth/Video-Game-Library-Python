class VideoGame:
    def __init__(self, title, genre, platform, release_year):
        self.title = title
        self.genre = genre
        self.platform = platform
        self.release_year = release_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Platform: {self.platform}")
        print(f"Release Year: {self.release_year}")
        print("-" * 20)

    def is_classic(self, current_year):
        """Check if the game is older than 5 years."""
        return current_year - self.release_year > 5
