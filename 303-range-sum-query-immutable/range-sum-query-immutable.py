class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg = [0] * (4 * self.n)
        def build(i, l, r):
            if l == r:
                self.seg[i] = nums[l]
                return
            mid = (l+r) // 2
            build(2* i, l, mid)
            build(2*i+1, mid+1, r)
            self.seg[i] = self.seg[2*i] + self.seg[2*i + 1]
            return
        build(1, 0 , len(nums) - 1)
        

    def sumRange(self, left: int, right: int) -> int:
        def query(i, l, r, left, right):
            if l>= left and r <= right:
                return self.seg[i]
            
            if r < left or l > right:
                return 0
            mid = (l+r) // 2
            left_sum = query(2*i, l, mid, left, right)
            right_sum = query(2*i + 1, mid+1, r, left, right)
            return left_sum + right_sum
        return query(1, 0, self.n - 1, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)