class MyStack:
    def __init__(self):
        self.q = collections.deque()
        self.len = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.len += 1

    def pop(self) -> int:
        self.len -= 1
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        if self.len == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()