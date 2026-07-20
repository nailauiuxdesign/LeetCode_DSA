import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned = set(banned)
        words = re.findall(r"\w+", paragraph.lower())
        count = Counter()
        for word in words:
            if word not in banned:
                count[word] += 1

        return count.most_common(1)[0][0]
