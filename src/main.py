from scrabble.game.game import Game
import pathlib
from scrabble.game.gaddag.gaddag import Gaddag

game = Game(15, "./resources/dictionaries/test_dict.txt")
print(game.dictionary)
print(game)

gaddag = Gaddag()

for word in game.dictionary:
    gaddag.add_word(word)

game.play()

print(game)

s = input()
while s:
    print(gaddag.lookup(s))
    s = input()