class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
            # Add a 0 at the beginning and end of the flowerbed
            # This makes it easier to handle edge cases without checking bounds
            flowerbed = [0] + flowerbed + [0]

            # Iterate from index 1 to len(flowerbed) - 2 to avoid checking the artificial 0s at ends
            for i in range(1, len(flowerbed) - 1):
                # Check if the current position and its adjacent plots are all empty
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1  # Plant a flower here
                    n -= 1            # Decrease the number of flowers we still need to plant

            # If we have planted enough flowers (n <= 0), return True; otherwise, return False
            return n <= 0
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # # Count how many flowers we still need to plant
            # for i in range(len(flowerbed)):
            #     # Check if current plot is empty
            #     if flowerbed[i] == 0:
            #      # Check if the left and right plots are also empty (or out of bounds)
            #         empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            #         empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

            #         # If both sides are empty, plant a flower here
            #         if empty_left and empty_right:
            #             flowerbed[i] = 1  # Plant the flower
            #             n -= 1            # One less flower to plant

            #             if n == 0:
            #                 return True   # We've planted all required flowers

            # # After the loop, check if we planted enough
            # return n <= 0
