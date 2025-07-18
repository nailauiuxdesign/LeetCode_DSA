class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get number of rows (m) and columns (n) in the matrix
        m, n = len(matrix), len(matrix[0])

        # Initialize left (l) and right (r) pointers for binary search
        # Treat the 2D matrix as a flattened 1D array from 0 to m*n - 1
        l, r = 0, m * n - 1

        # Perform binary search
        while l <= r:
          # Find the middle index in the "virtual" 1D array
            mid = (l + r) // 2

            # Convert the 1D mid index back to 2D coordinates (row and column)
            mid_i = mid // n  # row index
            mid_j = mid % n   # column index

            # Get the number at the mid position in the matrix
            #mid_num = matrix[mid_i][mid_j]

            # If the target is found, return True
            if target == matrix[mid_i][mid_j]:
                return True
                # If the target is greater, search the right half
            elif target > matrix[mid_i][mid_j]:
              l = mid + 1
            # If the target is smaller, search the left half
            else:
                r = mid - 1

        # If we exit the loop, the target was not found
        return False
