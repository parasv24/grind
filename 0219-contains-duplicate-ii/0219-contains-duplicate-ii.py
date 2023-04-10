class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0
        mp = {}
        k += 1
        while j < len(nums):
            mp[nums[j]] = mp.get(nums[j], 0) + 1
            if j - i + 1 < k:
                if len(mp) < j -i +1:
                    return True
                j += 1
            elif j - i + 1 == k:
                if len(mp) < k:
                    return True
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1
                j += 1
        return False