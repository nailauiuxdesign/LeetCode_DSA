from collections import Counter

class Solution:
    def canMerge(self, trees):
        roots = {t.val: t for t in trees}
        freq = Counter()

        for t in trees:
            freq[t.val] += 1
            if t.left:
                freq[t.left.val] += 1
            if t.right:
                freq[t.right.val] += 1

        def dfs(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            # merge only if it's a leaf AND another tree exists
            if not node.left and not node.right and node.val in roots:
                merge = roots.pop(node.val)
                node.left = merge.left
                node.right = merge.right

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        # find the real root
        for t in trees:
            if freq[t.val] == 1:
                roots.pop(t.val)          # ⭐ KEY FIX
                if dfs(t, float('-inf'), float('inf')) and not roots:
                    return t
                return None

        return None
