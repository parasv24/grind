class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        arr = [1]
        n -= 1
        mp = {}
        for el in primes:
            mp[el] = 0
        while n > 0:
            mini = 10000000000
            for el in primes:
                mini = min(mini, arr[mp[el]] * el)
            for el in primes:
                if arr[mp[el]] * el == mini:
                    mp[el] += 1
            arr.append(mini)
            n -= 1
        return arr[-1]
        