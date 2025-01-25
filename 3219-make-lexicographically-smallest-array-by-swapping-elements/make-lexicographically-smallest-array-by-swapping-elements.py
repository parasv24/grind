class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_with_idx = [[num, idx] for idx, num in enumerate(nums)]
        nums_with_idx.sort()
        color = [0] * len(nums)
        prev = nums_with_idx[0][0]
        col = 1
        color[nums_with_idx[0][1]] = 1
        mp = defaultdict(list)
        mp[col].append(prev)
        for num, idx in nums_with_idx[1:]:
            if abs(prev - num) > limit:
                col += 1
            color[idx] = col
            prev = num
            mp[col].append(num)
        ans = []
        idxs = defaultdict(int)
        for idx, num in enumerate(nums):
            col = color[idx]
            i = idxs[col]
            ans.append(mp[col][i])
            idxs[col] += 1
        return ans
