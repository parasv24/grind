class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            def get_prod(num):
                prod = 1
                while(num > 0):
                    prod = prod * (num % 10)
                    num = num // 10
                return prod
            if get_prod(n) % t == 0:
                return n
            n += 1
            
            
        