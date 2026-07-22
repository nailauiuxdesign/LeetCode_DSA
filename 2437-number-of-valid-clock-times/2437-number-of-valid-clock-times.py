class Solution:
    def countTime(self, time: str) -> int:
        ways = 1

        if time[3] == '?':
            ways *= 6
        if time[4] == '?':
            ways *= 10

        if time[0] == '?' and time[1] == '?':
            ways *= 24
        elif time[0] == '?':
            if time[1] <= '3':
                ways *= 3
            else:
                ways *= 2
        elif time[1] == '?':
            if time[0] == '2':
                ways *= 4
            else:
                ways *= 10
#
        return ways
