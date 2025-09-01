class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        counts = [0] * 26
 
        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
 
            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
 
            longest = max(longest, (r - l + 1))
 
        return longest
        
        
        
        # left = 0
        # max_freq = 0
        # max_window = 0
        # freq = defaultdict(int)
        # for right in range(len(s)):
        #     freq[s[right]] +=1
        #     max_freq = max(max_freq, freq[s[right]])
        #     if (right-left+1) - max_freq > k:
        #         freq[s[left]]-=1
        #         left+=1
        #     max_window= max(max_window, right-left+1)
        # return max_window