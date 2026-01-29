class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_le(mid):
            count = 0
            col = n - 1
            
            for row in range(n):
                while col >= 0 and matrix[row][col] > mid:
                    col -= 1
                count += (col + 1)
            
            return count

        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2
            
            if count_le(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
