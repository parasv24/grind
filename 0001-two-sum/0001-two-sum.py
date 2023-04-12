class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        arr = [[el, idx] for idx, el in enumerate(nums)]
        arr.sort(key = lambda x : x[0])
        while j > i:
            if arr[j][0] + arr[i][0] == target:
                return [arr[j][1], arr[i][1]]
            elif arr[j][0] + arr[i][0] > target:
                j -= 1
            else:
                i += 1
        