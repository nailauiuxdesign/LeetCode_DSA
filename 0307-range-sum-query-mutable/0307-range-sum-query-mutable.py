class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums[:]
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.add(i + 1, num)

    def add(self, i: int, value: int) -> None:
        while i < len(self.tree):
            self.tree[i] += value
            i += i & -i

    def get_sum(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def update(self, index: int, val: int) -> None:
        difference = val - self.nums[index]
        self.nums[index] = val
        self.add(index + 1, difference)

    def sumRange(self, left: int, right: int) -> int:
        return self.get_sum(right + 1) - self.get_sum(left)