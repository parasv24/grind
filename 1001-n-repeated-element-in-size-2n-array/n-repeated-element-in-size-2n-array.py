class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mp = {}
        for el in nums[:3]:
            if el in mp:
                return el
            mp[el] = 1
        maj = -1
        count = 0
        for el in nums[3:]:
            if count == 0:
                maj = el
                count = 1
            else:
                if el == maj:
                    count += 1
                else:
                    count -= 1
        return maj
        