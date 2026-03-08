class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            left, right = 0, n

            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1

            result.append(n - left)

        return result
        
