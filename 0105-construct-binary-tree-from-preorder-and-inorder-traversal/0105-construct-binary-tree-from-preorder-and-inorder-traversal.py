# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not preorder or not inorder:
            return None

        # locate root (first element of preorder)
        root = TreeNode(preorder[0])

        # find root index in inorder
        center = inorder.index(preorder[0])

        # recursively build left and right subtrees
        root.left = self.buildTree(preorder[1:center+1], inorder[:center])
        root.right = self.buildTree(preorder[center+1:], inorder[center+1:])

        return root