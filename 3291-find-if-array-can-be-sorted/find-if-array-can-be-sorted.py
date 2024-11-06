class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        arr = [[el, bin(el).count("1")] for el in nums]
        segs = [[nums[0]]]
        for i in range(1, len(arr)):
            if arr[i][1] == arr[i-1][1]:
                segs[-1].append(nums[i])
            else:
                segs.append([nums[i]])
        min_max_segs = [[min(seg), max(seg)] for seg in segs]
        flag = True
        for i in range(1, len(min_max_segs)):
            if min_max_segs[i][0] < min_max_segs[i-1][1]:
                flag = False
        return flag
        