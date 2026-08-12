class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        records = []

        for start in range(len(s2)):
            count = 0
            index = start
            for ch in s1:
                if ch == s2[index]:
                    index += 1

                    if index == len(s2):
                        count += 1
                        index = 0
            records.append((count, index))

        matches = 0
        index = 0
        for _ in range(n1):
            count, index = records[index]
            matches += count

        return matches // n2