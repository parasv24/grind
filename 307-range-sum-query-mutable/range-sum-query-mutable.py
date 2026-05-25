class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.block_size = ceil(sqrt(len(nums)))
        self.blocks = [0] * (ceil(len(nums) / self.block_size))
        for i in range(len(nums)):
            self.blocks[i // self.block_size] += nums[i]

        

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.blocks[index // self.block_size] += diff
        

    def sumRange(self, left: int, right: int) -> int:
        # print(left, right, self.block_size, self.blocks, self.nums)
        ans = 0
        while left % self.block_size != 0 and left <= right:
            ans += self.nums[left]
            left += 1
        
        while left + self.block_size <= right:
            ans += self.blocks[left // self.block_size]
            left += self.block_size
        
        while left <= right:
            ans += self.nums[left]
            left += 1
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)