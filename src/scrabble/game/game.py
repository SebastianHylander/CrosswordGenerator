import random
import threading

from scrabble.game.gaddag.gaddag import Gaddag, SPECIAL_CHAR
class Game:
    def __init__(self, size, dictionary_path):
        self.size = size
        self.board = [['#' for _ in range(size)] for _ in range(size)]
        self.dictionary = self._get_dictionary(dictionary_path)
        self.gaddag = self._get_gaddag()
    
    def _get_dictionary(self, dictionary_path):
        dictionary = self._read_dictionary(dictionary_path)
        return {word for word in dictionary if len(word) <= self.size}

    def _read_dictionary(self, dictionary_path):
        with open(dictionary_path, "r") as file:
            return set(word.strip() for word in file)
    
    def _get_gaddag(self):
        gaddag = Gaddag()
        for word in self.dictionary:
            gaddag.add_word(word)
        return gaddag
        
    def __str__(self):
        return "\n".join(" ".join(row) for row in self.board)
    
    def add_participant(self, participant):
        self.participants.append(participant)
    
    def play(self):
        self._place_first_word()
        words = self._find_words()
        while words:
            word = self._get_best_word(words)
            for tile in word:
                x = tile[0][0]
                y = tile[0][1]
                self.board[y][x] = tile[1]
            words = self._find_words()

    def _place_first_word(self):
        x = random.randint(0, self.size-1)
        word = random.choice(list(self.dictionary))
        for y in range(len(word)):
            self.board[y][x] = word[y]
    
    def _find_words(self):
        start_positions_x = []
        start_positions_y = []
        for row in range(self.size):
            for col in range(self.size):
                if not self.board[row][col] == SPECIAL_CHAR:
                    if col == self.size-1 or self.board[row][col+1] == SPECIAL_CHAR:
                        start_positions_x.append((col, row))
                    if row == self.size-1 or self.board[row+1][col] == SPECIAL_CHAR:
                        start_positions_y.append((col, row))

    



    def _get_best_word(self, words):
        return random.choice(words)
