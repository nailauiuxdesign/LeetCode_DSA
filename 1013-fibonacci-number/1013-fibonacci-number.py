class Solution:
    def fib(self, n: int) -> int:
        # previous, current = 0, 1
      
        # for _ in range(n):
        #     previous, current = current, previous + current
      
        # return previous

        # Base case: 0 or 1
        if n == 0 or n == 1:
            return n
        # Recursive case: sum of two previous numbers
        return self.fib(n - 1) + self.fib(n - 2)

