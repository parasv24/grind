class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def num_of_cycles(a, b):
            return a if b == 0 else num_of_cycles(b, a % b)
        n = len(nums)
        k %= n
        i = 0
        if k == 0:
            return
        else:
            cycles = num_of_cycles(n, k)
            print(cycles)
            for i in range(0, cycles):
                j, prev = i + k, nums[i]
                while j != i:
                    nums[j], prev = prev, nums[j]
                    j += k
                    j %= n
                nums[j] = prev