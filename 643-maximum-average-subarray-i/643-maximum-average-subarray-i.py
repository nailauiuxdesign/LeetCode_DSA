class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        num = len(nums)  # Total length of nums
        current_sum = 0  # Sum of the current window of size k

        # Step 1: Calculate sum of the first k elements
        for i in range(k):
            current_sum += nums[i]

        max_avg = current_sum / k # Initialize max average with the first window's average

        # Step 2: Slide the window from k to end of array
        for i in range(k, num):
            current_sum += nums[i] # Add new element to window
            current_sum -= nums[i - k] # Remove element that slid out of window

            avg = current_sum / k  # Calculate current average
            max_avg = max(max_avg, avg) # Update max average if current is greater

        return max_avg # Return the highest average found
    
