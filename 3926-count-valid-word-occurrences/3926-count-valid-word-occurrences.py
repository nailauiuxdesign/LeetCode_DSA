from collections import defaultdict

class Solution:
    def countWordOccurrences(self, chunks, queries):
        text = "".join(chunks)
        count = defaultdict(int)

        i = 0
        while i < len(text):
            if text[i] == " " or text[i] == "-":
                i += 1
                continue

            word = ""
            while i < len(text):
                if text[i] == " ":
                    break
                if text[i] == "-":
                    if i + 1 == len(text) or text[i + 1] == " " or text[i + 1] == "-":
                        break
                word += text[i]
                i += 1
            count[word] += 1

        answer = []
        for word in queries:
            answer.append(count[word])

        return answer
