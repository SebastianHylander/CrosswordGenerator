from scrabble.game.game import Game
import pathlib

game = Game(15, "./resources/dictionaries/test_dict.txt")
print(game.dictionary)