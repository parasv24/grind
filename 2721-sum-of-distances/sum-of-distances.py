class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            if not nums[i] in mp:
                mp[nums[i]] = []
            prev = mp[nums[i]][-1][1] if len(mp[nums[i]]) > 0 else 0
            mp[nums[i]].append([i, prev + i])
        print(mp)
        ans = [0] * len(nums)
        for key in mp.keys():
            if len(mp[key]) > 1:
                for i in range(len(mp[key])):
                    left_ans, right_ans = 0, 0
                    if i > 0:
                        left_ans = (mp[key][i][0] * i) - mp[key][i-1][1]
                    if i + 1 < len(mp[key]):
                        right_ans = (mp[key][-1][1] - mp[key][i][1]) - (mp[key][i][0] * (len(mp[key]) - i - 1))
                    ans[mp[key][i][0]]= left_ans + right_ans
        return ans
                
                        

            


        

        