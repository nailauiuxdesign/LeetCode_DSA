class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #define hashmap
        count = {}
        #arr_bucket_sort
        freq = [[] for i in range(len(nums) + 1)]
        #in count, element and count
        #5 not in hashmap
        {5:1}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        #[1,1,1,2,2,3]

        # (1:3, 2: 2, 3:1)
        # add element at the index as count
        for num, cnt in count.items():
            freq[cnt].append(num)
        #traverse on freq

        #traverse in decreasing order
        result = []
        for i in range(len(freq)-1, 0, -1):
            #inside list traverse
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
      