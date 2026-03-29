class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        facts = [1]
        prev = 1
        MOD = 1000000007
        for i in range(1, 100000):
            prev = (prev * i) % MOD
            facts.append(prev)
        divis = pow((facts[k] * facts[n-1-k]), MOD - 2, MOD)
        return (facts[n-1] * 2 * divis) % MOD
        