class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        cnt = 0
        for el in nums:
            if el < pivot:
                ans.append(el)
            if el == pivot:
                cnt += 1
        ans += [pivot] * cnt
        for el in nums:
            if el > pivot:
                ans.append(el)
        return ans