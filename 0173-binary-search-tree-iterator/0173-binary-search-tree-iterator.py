class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        cur_node = self.stack.pop()
        cur = cur_node.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return cur_node.val

    def hasNext(self):
        return self.stack != []