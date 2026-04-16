class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        mp = defaultdict(list)
        idxs = [0] * len(nums)
        for idx, el in enumerate(nums):
            if len(mp[el]) == 0:
                cur_idx = 0
            else:
                _, pre = mp[el][-1]
                cur_idx = pre + 1
            mp[el].append([idx, cur_idx])
            idxs[idx] = cur_idx
        
        ans = []
        for query in queries:
            key = nums[query]
            idx = idxs[query]
            if len(mp[key]) == 1:
                ans.append(-1)
            else:
                # print(query, mp[key], idx)
                cur, _ = mp[key][idx]
                sub_ans = len(nums)
                pre_idx, cur_idx = idx - 1 , (idx + 1) % len(mp[key])
                # print(pre_idx, cur_idx)
                pre , _ = mp[key][pre_idx]
                sub_ans = min(sub_ans, abs(cur - pre) , abs(len(nums) - pre + cur))
                nxt, _ = mp[key][cur_idx]
                sub_ans = min(sub_ans, abs(nxt - cur) , abs(len(nums) - cur + nxt))
                ans.append(sub_ans)
        return ans
        