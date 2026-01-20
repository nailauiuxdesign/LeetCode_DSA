class TreeAncestor:
    def __init__(self, n: int, parent: list[int]):
        self.LOG = n.bit_length()
        self.dp = [[-1] * self.LOG for _ in range(n)]

        for i in range(n):
            self.dp[i][0] = parent[i]
        for j in range(1, self.LOG):
            for i in range(n):
                prev = self.dp[i][j - 1]
                if prev != -1:
                    self.dp[i][j] = self.dp[prev][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        bit = 0
        while node != -1 and k:
            if k & 1:
                node = self.dp[node][bit]
            k >>= 1
            bit += 1
        return node
