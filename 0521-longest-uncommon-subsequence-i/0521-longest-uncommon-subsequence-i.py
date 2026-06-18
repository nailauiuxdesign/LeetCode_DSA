class Solution:
    def findLUSlength(self, a, b):
        if a == b:
            return -1
            
        if len(a) > len(b):
            return len(a)

        return len(b)