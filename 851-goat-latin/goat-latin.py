class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        result = []
        words = sentence.split()

        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                goat_word = word
            else:
                goat_word = word[1:] + word[0]
            goat_word += "ma" + "a" * (i + 1)
            result.append(goat_word)

        return " ".join(result)