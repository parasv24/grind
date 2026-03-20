class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]
        arr = [1]
        n -= 1
        idxs = {}
        mp = {}
        for el in primes:
            mp[el] = []
            idxs[el] = 0
        while n > 0:
            mini = 100000000000
            for el in primes:
                mp[el].append(arr[-1] * el)
            for el in primes:
                mini = min(mini, mp[el][idxs[el]])
            for el in primes:
                if mp[el][idxs[el]] == mini:
                    idxs[el] += 1
            # print(arr, mp, idxs, mini)
            arr.append(mini)
            n -= 1
        return arr[-1]
        