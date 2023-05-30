class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            return f(n-1) + f(n-2) if n > 1 else n
        return f(n)