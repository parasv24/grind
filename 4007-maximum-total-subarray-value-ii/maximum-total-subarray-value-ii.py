class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seg = [0] * (4 * n)
        def build(i, l, r):
            if l == r:
                seg[i] = (nums[l], nums[l])
                return
            mid = (l+r) // 2
            build(i*2 + 1, l , mid)
            build(i*2 + 2, mid+1, r)
            seg[i] = (max(seg[i*2+1][0], seg[i*2+2][0]), min(seg[i*2+1][1], seg[i*2+2][1]))
            return
        
        def query(i, l, r, left, right):
            if l > right or r < left:
                return (-1, 10 ** 12)
            if left <= l and r <= right:
                return seg[i]
            
            mid = (l + r) // 2
            left_max, left_min = query(2*i + 1, l, mid, left, right)
            right_max, right_min = query(2*i + 2, mid + 1, r, left, right)
            return (max(left_max, right_max), min(left_min, right_min))


        build(0, 0, n-1)

        total = 0
        mx, mn = query(0, 0, n-1, 0, n-1)
        hp = [[mn - mx, 0, n-1]]
        ans = 0
        st = set()
        st.add((0,n-1))
        while k > 0:
            val , l, r = heappop(hp)
            ans += abs(val)
            if l < r:
                if (l, r-1) not in st:
                    mx, mn = query(0, 0, n-1, l, r-1)
                    heapq.heappush(hp, [mn - mx, l, r-1])
                    st.add((l, r-1))
                if (l+1, r) not in st:
                    mx, mn = query(0, 0, n-1, l+1, r)
                    heapq.heappush(hp, [mn-mx, l+1, r])
                    st.add((l+1, r))
            k -= 1
        return ans
        

        