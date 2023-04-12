class Solution:
    dp = {}
    def fib(self, n: int) -> int:
        ans = self.dp.get(n, -1) 
        if ans!= -1:
            return ans
        return self.fib(n-1) + self.fib(n-2) if n > 1 else n
        