class Solution:
    def findLUSlength(self, strs):

        def isSub(a, b):
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
            return i == len(a)

        duplicates = set()
        for word in strs:
            if strs.count(word) > 1:
                duplicates.add(word)

        strs.sort(key=len, reverse=True)

        for i in range(len(strs)):
            if strs[i] in duplicates:
                continue
            found = False
            for j in range(i):
                if isSub(strs[i], strs[j]):
                    found = True
                    break
            if not found:
                return len(strs[i])

        return -1