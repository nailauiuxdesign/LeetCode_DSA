# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def traverse(node, low = float('-inf'), high = float('inf')):
            nonlocal ans
            if not node:
                return
            if node.val<=low or node.val>=high:
                ans = False
            traverse(node.left,low,node.val)
            traverse(node.right,node.val, high)
        traverse(root)
        return ans

        # def is_valid(node, minn, maxx):
        #     if not node:
        #         return True
            
        #     if node.val <= minn or node.val >= maxx:
        #         return False
            
        #     return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)
 
        # return is_valid(root, float("-inf"), float("inf"))