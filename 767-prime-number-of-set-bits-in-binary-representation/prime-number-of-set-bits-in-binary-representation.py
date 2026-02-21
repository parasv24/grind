class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = [True for i in range(33)]
        primes[0] = primes[1] = False
        p = 2
        while(p * p <= 32):
            if primes[p]:
                for j in range(p * p, 33, p):
                    primes[j] = False
            p += 1
        def count_bits(n):
            ans = 0
            while n > 0:
                n , mod = divmod(n, 2)
                if mod == 1:
                    ans += 1
            return ans
        ans = 0
        for el in range(left, right + 1):
            bits = count_bits(el)
            # prin
            if primes[bits]:
                ans += 1
        return ans
        