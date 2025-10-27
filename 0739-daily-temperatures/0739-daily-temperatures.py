class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        answer = [0] * len(temperatures)
        stk = []
 
        for i, temp in enumerate(temperatures):
            while stk and stk[-1][0] < temp:
                stk_t, stk_i = stk.pop()
                answer[stk_i] = i - stk_i
 
            stk.append((temp, i))
        return answer