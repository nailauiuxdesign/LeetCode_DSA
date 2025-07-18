class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
            # Count how many flowers we still need to plant
            for i in range(len(flowerbed)):
                # Check if current plot is empty
                if flowerbed[i] == 0:
                 # Check if the left and right plots are also empty (or out of bounds)
                    empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                    empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                    # If both sides are empty, plant a flower here
                    if empty_left and empty_right:
                        flowerbed[i] = 1  # Plant the flower
                        n -= 1            # One less flower to plant

                        if n == 0:
                            return True   # We've planted all required flowers

            # After the loop, check if we planted enough
            return n <= 0
