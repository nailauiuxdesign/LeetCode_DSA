class Solution:
    def pathSum(self, root, targetSum):
        def countPaths(node, remaining):
            if not node:
                return 0

            count = 0

            if node.val == remaining:
                count += 1
            count += countPaths(node.left, remaining - node.val)
            count += countPaths(node.right, remaining - node.val)
            return count

        if not root:
            return 0

        paths_from_root = countPaths(root, targetSum)
        left_paths = self.pathSum(root.left, targetSum)
        right_paths = self.pathSum(root.right, targetSum)

        return paths_from_root + left_paths + right_paths