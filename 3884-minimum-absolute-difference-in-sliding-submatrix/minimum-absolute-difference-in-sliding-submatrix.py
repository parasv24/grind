class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for i in range(len(grid) - k + 1):
            sub_ans = []
            for j in range(len(grid[0]) - k + 1):
                mp = {}
                for idxx in range(i , i + k):
                    for idxy in range(j, j+k):
                        mp[grid[idxx][idxy]]=1
                nums = sorted(mp.keys())
                if len(nums) == 1:
                    sub_ans.append(0)
                else:
                    sub_ans.append(min([abs(j-i) for i,j in zip(nums, nums[1:])]))
            ans.append(sub_ans)
        return ans



        