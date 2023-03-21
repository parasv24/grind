class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n - 1
        ss = [0 for _ in range(0,n)]
        k = n
        while(i<=j):
            k -= 1
            x = nums[i] * nums[i]
            y = nums[j] * nums[j]
            if(x< y):
                ss[k] = y
                j -= 1
            else:
                ss[k] = x
                i += 1
        return ss   