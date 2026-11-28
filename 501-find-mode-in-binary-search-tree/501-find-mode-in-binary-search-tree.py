# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        result = []
        previous = None
        count = 0
        max_count = 0

        def inorder(node):
            nonlocal previous, count, max_count

            if not node:
                return

            inorder(node.left)
            if previous == node.val:
                count += 1
            else:
                count = 1

            if count > max_count:
                max_count = count
                result.clear()
                result.append(node.val)
            elif count == max_count:
                result.append(node.val)

            previous = node.val
            inorder(node.right)

        inorder(root)
        return result
