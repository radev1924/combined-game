import sys

from game import AsciiMode, Pygamemode, CombinedMode

if __name__ == "main":
    try:
        game_mode = sys.argv[1]
        game = AsciiMode() if game_mode = "ascii" else Pygamemode()
    except IndexError:
        game = CombinedMode
    game.run()