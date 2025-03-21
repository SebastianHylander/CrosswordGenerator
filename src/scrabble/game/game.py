class Game:
    def __init__(self, size, dictionary_path):
        self.size = size
        self.board = [['#' for _ in range(size)] for _ in range(size)]
        self.dictionary = self._read_dictionary(dictionary_path)
    
    def _read_dictionary(self, dictionary_path):
        with open(dictionary_path, "r") as file:
            return set(word.strip() for word in file)
        
    def __str__(self):
        return "\n".join(" ".join(row) for row in self.board)