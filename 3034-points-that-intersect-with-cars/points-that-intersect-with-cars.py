class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = [0]* 102
        for x, y in nums:
            ans[x] += 1
            ans[y+1] -= 1
        cnt = 0
        for i in range(1,101):
            ans[i]+= ans[i-1]
            if ans[i] > 0:
                cnt += 1
        return cnt


        