class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                ans = "Fizz"
                if i % 5 == 0:
                    ans += "Buzz"
            elif i % 5 == 0:
                ans = "Buzz"
            else:
                ans = str(i)
            res.append(ans)
        print(res)
        return res