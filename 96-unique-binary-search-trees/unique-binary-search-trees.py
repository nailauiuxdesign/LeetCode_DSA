class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [0] * (n + 1)
        numTree[0] = 1
        numTree[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                numTree[nodes] += numTree[root - 1] * numTree[nodes - root]

        return numTree[n]
