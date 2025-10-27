class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        ans=[0]*len(temperatures)
        stack=[]

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                d,t=stack.pop()
                ans[d]=(i-d)
            stack.append([i,temp])
        return ans