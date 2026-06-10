class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # seg = [0] * (4 * n)
        # def build(i, l, r):
        #     if l == r:
        #         seg[i] = (nums[l], nums[l])
        #         return
        #     mid = (l+r) // 2
        #     build(i*2 + 1, l , mid)
        #     build(i*2 + 2, mid+1, r)
        #     seg[i] = (max(seg[i*2+1][0], seg[i*2+2][0]), min(seg[i*2+1][1], seg[i*2+2][1]))
        #     return
        
        # def query(i, l, r, left, right):
        #     if l > right or r < left:
        #         return (-1, 10 ** 12)
        #     if left <= l and r <= right:
        #         return seg[i]
            
        #     mid = (l + r) // 2
        #     left_max, left_min = query(2*i + 1, l, mid, left, right)
        #     right_max, right_min = query(2*i + 2, mid + 1, r, left, right)
        #     return (max(left_max, right_max), min(left_min, right_min))


        # build(0, 0, n-1)

        # total = 0
        # mx, mn = query(0, 0, n-1, 0, n-1)
        # hp = [[mn - mx, 0, n-1]]
        # ans = 0
        # st = set()
        # st.add((0,n-1))
        # while k > 0:
        #     val , l, r = heappop(hp)
        #     ans += abs(val)
        #     if l < r:
        #         if (l, r-1) not in st:
        #             mx, mn = query(0, 0, n-1, l, r-1)
        #             heapq.heappush(hp, [mn - mx, l, r-1])
        #             st.add((l, r-1))
        #         if (l+1, r) not in st:
        #             mx, mn = query(0, 0, n-1, l+1, r)
        #             heapq.heappush(hp, [mn-mx, l+1, r])
        #             st.add((l+1, r))
        #     k -= 1
        # return ans
        
        # SQRT DECOMPOSITION T.L.E
        # n = len(nums)
        # block_size = ceil(sqrt(n))
        # blocks = [(-1, 10**12) for _ in range((n - 1)//block_size + 1)]
        # l = 0

        # while l < n:
        #     mx, mn = blocks[l//block_size]
        #     blocks[l//block_size] = (max(mx, nums[l]), min(mn, nums[l]))
        #     l += 1

        # def query(l, r):
        #     mx, mn = -1, 10 ** 12
        #     while l % block_size != 0 and l <= r:
        #         mx = max(mx, nums[l])
        #         mn = min(mn, nums[l])
        #         l += 1
            
        #     while l + block_size <= r:
        #         bmx, bmin = blocks[l // block_size]
        #         mx = max(mx, bmx)
        #         mn = min(mn, bmin)
        #         l += block_size

        #     while l <= r:
        #         mx = max(mx, nums[l])
        #         mn = min(mn, nums[l])
        #         l += 1
        #     return (mx, mn)
        
        # total = 0
        # mx, mn = query(0, n-1)
        # hp = [(mn - mx, 0, n-1)]
        # ans = 0
        # st = set()
        # st.add((0,n-1))
        # if k >= n * (n + 1) // 2 - n:
        #     k = n * (n + 1) // 2 - n
        # while k > 0:
        #     val , l, r = heappop(hp)
        #     ans += abs(val)
        #     if l < r:
        #         if (l, r-1) not in st:
        #             mx, mn = query(l, r-1)
        #             heapq.heappush(hp, (mn - mx, l, r-1))
        #             st.add((l, r-1))
        #         if (l+1, r) not in st:
        #             mx, mn = query(l+1, r)
        #             heapq.heappush(hp, (mn-mx, l+1, r))
        #             st.add((l+1, r))
        #     k -= 1
        # return ans
        
        # SPARSE TABLE

        n = len(nums)
        logn = n.bit_length()
        table = [[] for _ in range(logn)]
        for i in range(len(nums)):
            table[0].append((nums[i], nums[i]))
        
        for i in range(1, logn):
            jump = 1 << (i - 1)
            length = 1 << i
            for j in range(n - length + 1):
                left = table[i - 1][j]
                right = table[i - 1][j + jump]

                mx = max(left[0], right[0])
                mn = min(left[1], right[1])

                table[i].append((mx, mn))


        def query(l, r):
            length = r - l + 1
            span = length.bit_length() - 1

            left = table[span][l]
            right = table[span][r - (1 << span) + 1]

            mx = max(left[0], right[0])
            mn = min(left[1], right[1])

            return mx, mn
        
        total = 0
        mx, mn = query(0, n-1)
        hp = [(mn - mx, 0, n-1)]
        ans = 0
        st = set()
        st.add((0,n-1))
        if k >= n * (n + 1) // 2 - n:
            k = n * (n + 1) // 2 - n
        while k > 0:
            val , l, r = heappop(hp)
            ans += abs(val)
            if l < r:
                if (l, r-1) not in st:
                    mx, mn = query(l, r-1)
                    heapq.heappush(hp, (mn - mx, l, r-1))
                    st.add((l, r-1))
                if (l+1, r) not in st:
                    mx, mn = query(l+1, r)
                    heapq.heappush(hp, (mn-mx, l+1, r))
                    st.add((l+1, r))
            k -= 1
        return ans




        