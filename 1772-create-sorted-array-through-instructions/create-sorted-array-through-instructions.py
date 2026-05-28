class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = max(instructions) + 1
        MOD = 10 ** 9 + 7
        seg = [0] * (4 * n)
        def insert(i, l, r, val):
            if l == r and l == val:
                seg[i] += 1
                return
            
            mid  = (l+r) // 2
            if val <= mid:
                insert(i*2, l, mid, val)
            else:
                insert(i*2+1, mid+1, r, val)
            seg[i] = seg[i*2] + seg[i*2 + 1]
            return
        
        def query(i, l, r, left, right):
            if left <= l and r <= right:
                return seg[i]
            
            if r < left or l > right:
                return 0
            mid = (l+r) // 2
            left_ans = query(i*2, l, mid, left, right)
            right_ans = query(i*2+1, mid+1, r, left, right)
            return left_ans + right_ans
        
        ans = 0
        for el in instructions:
            mins = query(1, 0, n-1, 0, el - 1)
            maxs = query(1, 0, n-1, el+1, n-1)
            ans += min(mins, maxs)
            insert(1, 0, n-1, el)
        return ans % MOD
