# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        n = 0

        # Loop until we have processed all nodes
        while curr or stack:
            # Go to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            # Process the node at the top of the stack
            small = stack.pop()
            n += 1

            if n == k:
                return small.val

            # Move to the right subtree
            curr = small.right
       