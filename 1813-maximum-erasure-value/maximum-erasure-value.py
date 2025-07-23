class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0   # Stores the maximum sum of a subarray with unique elements
        current_sum = 0   # Current window sum
        seen = set()    # Set to track unique elements in the current window
        l = 0   # Left pointer of the sliding window

        for r in range(len(nums)):   # Iterate through the array using right pointer
            while nums[r] in seen:   # If duplicate is found, shrink window from the left until it's removed
                current_sum -= nums[l]   # Subtract the leftmost element from the score
                seen.remove(nums[l])    # Remove it from the set
                l += 1  # Move the left pointer forward

            seen.add(nums[r])   # Add the current number to the window
            current_sum += nums[r] 
            max_score = max(max_score, current_sum)   # Update the answer with the maximum score seen so far

        return max_score    # Return the max score of subarrays with all unique elements







        # max_score = 0   # Stores the maximum sum of a subarray with unique elements
        # current_sum = 0   # Current window sum
        # seen = set()    # Set to track unique elements in the current window
        # l = 0   # Left pointer of the sliding window
        # n = len(nums)
        # for r in range(n):   # Iterate through the array using right pointer
        #     current_sum += nums[r]
        #     while nums[r] in seen:   # If duplicate is found, shrink window from the left until it's removed
        #         seen.remove(nums[l])    # Remove it from the set
        #         current_sum -= nums[l]   # Subtract the leftmost element from the score
        #         #seen.remove(nums[l])    # Remove it from the set
        #         l += 1  # Move the left pointer forward

        #     seen.add(nums[r])   # Add the current number to the window
        #     #current_sum += nums[r] 
        #     max_score = max(max_score, current_sum)   # Update the answer with the maximum score seen so far

        # return max_score    # Return the max score of subarrays with all unique elements
