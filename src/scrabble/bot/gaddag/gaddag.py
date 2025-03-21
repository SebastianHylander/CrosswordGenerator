SPECIAL_CHAR = '#' # chr(0)

class Gaddag:
    def __init__(self, is_terminal=False):
        self.is_terminal = is_terminal
        self.children = {}
    
    def add_word(self, word):
        words = [word[i::-1]+ SPECIAL_CHAR + word[i+1:] for i in range(len(word))]
        for w in words:
            self._add_word(w)

    def _add_word(self, word):
        print(word)
        if not word:
            self.is_terminal = True
            return
        c = word[0]
        self._get_or_default_child(c)._add_word(word[1:])
        
    def _get_or_default_child(self, c):
        if c not in self.children:
            self.children[c] = Gaddag()
        return self.children[c]
    
    def lookup(self, word):
        child = self.step(word[0])
        if not child:
            return False
        if child.reverse():
            return child.reverse().search(word[1:])
        return False
    
    def search(self, word):
        if not word:
            return self.is_terminal
        c = word[0]
        if self.step(c):
            return self.step(c).search(word[1:])
        return False
    
    def step(self, c):
        return self.children.get(c, None)
    
    def reverse(self):
        return self.step(SPECIAL_CHAR)