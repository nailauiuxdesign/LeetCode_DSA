# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0   # Tracks root index in preorder

        def build(left: int, right: int) -> Optional[TreeNode]:
            # If no elements remain in this subtree
            if left > right:
                return None

            # Pick current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Split inorder into left and right subtrees
            mid = inorder_map[root_val]

            # Recursively build left and right children
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
