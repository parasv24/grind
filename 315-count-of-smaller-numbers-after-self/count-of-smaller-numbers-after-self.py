class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = 3 * (10 ** 4)
        seg = [0] * (4*n)
        def insert(i, l, r, val):
            if l == r:
                seg[i] += 1
                return 
            mid = (l + r) // 2
            if val <= mid:
                insert(2*i, l, mid, val)
            else:
                insert(2*i+1, mid+1, r, val)
            seg[i] = seg[i*2] + seg[i*2 + 1]
            return
        def query(i, l, r, left, right):
            if left <= l and r <= right:
                return seg[i]
            
            if r < left or l > right:
                return 0
            mid = (l+r) // 2
            left_ans = query(i*2, l, mid, left, right)
            right_ans = query(i*2 + 1, mid + 1, r, left, right)
            return left_ans + right_ans
        
        ans = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            val = query(1, 0, n-1, 0, nums[i] - 1 + 10 ** 4)
            ans[i] = val
            insert(1, 0, n-1, nums[i] + 10 ** 4)
        return ans
        