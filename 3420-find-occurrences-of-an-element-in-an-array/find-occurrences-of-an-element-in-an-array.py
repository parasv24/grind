class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        mp = {}
        occ = 1
        for i in range(len(nums)):
            if nums[i] == x:
                mp[occ] = i
                occ += 1
        ans = []
        for el in queries:
            ans.append(mp.get(el, -1))
        return ans
        