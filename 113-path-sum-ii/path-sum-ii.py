class Solution:
    def pathSum(self, root, targetSum):
        result = []
        path = []
        def dfs(node, remaining):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val == remaining:
                result.append(path.copy())
            else:
                dfs(node.left, remaining - node.val)
                dfs(node.right, remaining - node.val)
            path.pop()
        dfs(root, targetSum)
        return result