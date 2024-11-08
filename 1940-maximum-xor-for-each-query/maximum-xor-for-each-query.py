class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        total_xor = nums[0]
        for i in range(1, len(nums)):
            total_xor ^= nums[i]

        for i in range(0, len(nums)):
            bin_rep = str(bin(total_xor))[2:]
            answer = ""
            if len(bin_rep) < maximumBit:
                bin_rep = "0" * (maximumBit - len(bin_rep)) + bin_rep 
            for k in range(0, maximumBit):
                answer += str((int(bin_rep[k]) + 1) % 2)
            ans.append(int(answer,2))
            total_xor ^= nums[len(nums) - i - 1]
        return ans