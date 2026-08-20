class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        if n == 0:
            return []

        def build(start, end):
            if start > end:
                return [None]

            trees = []
            for root in range(start, end + 1):
                left_trees = build(start, root - 1)
                right_trees = build(root + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        root_node = TreeNode(root)
                        root_node.left = left
                        root_node.right = right
                        trees.append(root_node)
            return trees

        return build(1, n)