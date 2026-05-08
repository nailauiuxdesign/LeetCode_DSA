class MagicDictionary:
    def __init__(self):
        self.words = {}

    def buildDict(self, dictionary):
        for word in dictionary:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                if pattern in self.words:
                    self.words[pattern] = "*"
                else:
                    self.words[pattern] = word[i]

    def search(self, searchWord):
        for i in range(len(searchWord)):
            pattern = searchWord[:i] + "*" + searchWord[i + 1:]
            if pattern in self.words:
                if self.words[pattern] != searchWord[i]:
                    return True
        return False
