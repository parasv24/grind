class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n % 2 != 0:
            ans.append(0)
            n -= 1
        i = 1
        while n > 0:
            n-=2
            ans += [i, -i]
            i += 1
        return ans