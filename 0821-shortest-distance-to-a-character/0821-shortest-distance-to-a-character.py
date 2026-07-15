class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [0] * n
        last = -n
        for i in range(n):
            if s[i] == c:
                last = i
            answer[i] = i - last

        last = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last = i
            answer[i] = min(answer[i], last - i)

        return answer