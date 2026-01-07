class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p = 0
        for num in nums:
            if (p >> (num - 1)) & 1:
                return num
            p |= (1 << (num - 1)) 

            

        