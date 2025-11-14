class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, n):
            if len(n) == len(digits):
                ans.append(n)
                return
 
            for letter in letter_map[digits[i]]:
                backtrack(i + 1, n + letter)
 
        if digits:
            backtrack(0, "")

        return ans