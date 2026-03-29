class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        return (comb(n-1,k) * 2) % 1000000007
        