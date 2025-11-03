# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, float('-inf'), float('inf'))

    def _isValidBST(self, node: TreeNode, min_val: float, max_val: float) -> bool:
        if not node:
            return True

        if not (min_val < node.val < max_val):
            return False

        return (self._isValidBST(node.left, min_val, node.val) and
                self._isValidBST(node.right, node.val, max_val))

    
        # def is_valid(node, minn, maxx):
        #     if not node:
        #         return True
            
        #     if node.val <= minn or node.val >= maxx:
        #         return False
            
        #     return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)
 
        # return is_valid(root, float("-inf"), float("inf"))