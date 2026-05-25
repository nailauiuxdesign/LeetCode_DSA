class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        values = set()
        for i, char in enumerate(s):
            if char not in d:
                if t[i] in values:
                    return False
                d[char] = t[i]
                values.add(t[i])
            else:
                if d[char] != t[i]:
                    return False

        return True

class Solution:
    def isIsomorphic(self, s, t):
        mapping = {}
        values = set()

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 in mapping:
                if mapping[ch1] != ch2:
                    return False
            else:
                if ch2 in values:
                    return False
                mapping[ch1] = ch2
                values.add(ch2)

        return True