class Solution:
    def countPrimes(self, n: int) -> int:
        # if n <= 2:
        #     return 0
        # ans = 1
        # for i in range(3, n, 2):
        #     prime = 1
        #     for j in range(3, int(i**0.5) + 1, 2):
        #         if i % j == 0:
        #             prime = 0
        #             break
        #     ans += prime
        # return ans
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2, n):
            if prime[i]:
                for multiple in range(i + i, n, i):
                    # print(multiple, n)
                    prime[multiple] = False
        # print(prime)
        return sum(prime[2:])
        