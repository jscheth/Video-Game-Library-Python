from video_game import VideoGame
from library import VideoGameLibrary

def main():
    # Create games
    game1 = VideoGame("The Legend of Zelda", "Adventure", "Nintendo Switch", 2017)
    game2 = VideoGame("Minecraft", "Sandbox", "PC", 2011)
    game3 = VideoGame("FIFA 23", "Sports", "PlayStation 5", 2022)

    # Create a library and add games
    library = VideoGameLibrary()
    library.add_game(game1)
    library.add_game(game2)
    library.add_game(game3)

    # Display all games
    print("🎮 All Games in Library:")
    library.display_all_games()

    # Show classics
    print("\n🎮 Classic Games (older than 5 years):")
    library.show_classics(2025)

if __name__ == "__main__":
    main()