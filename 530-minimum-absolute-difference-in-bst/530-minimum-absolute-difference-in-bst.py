# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_dis = float('inf')  # Initialize minimum difference to infinity
        self.prev_val = None          # Initialize previous value

        def inorder_traversal(node):
            nonlocal self
            if not node:
                return

            inorder_traversal(node.left) # Traverse left subtree

            if self.prev_val is not None: # Process current node
                self.min_dis = min(self.min_dis, abs(node.val - self.prev_val))
            self.prev_val = node.val

            inorder_traversal(node.right) # Traverse right subtree

        inorder_traversal(root)
        return self.min_dis
