class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        arr = [1]
        n -= 1
        idxs = {}
        mp = {}
        for el in primes:
            mp[el] = []
            idxs[el] = 0
        while n > 0:
            mini = 10000000000
            for el in primes:
                mp[el].append(arr[-1] * el)
            for el in primes:
                mini = min(mini, mp[el][idxs[el]])
            for el in primes:
                if mp[el][idxs[el]] == mini:
                    idxs[el] += 1
            arr.append(mini)
            n -= 1
        return arr[-1]
        