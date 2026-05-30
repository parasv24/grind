class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Brute de force
        # obs = []
        # for query in queries:
        #     if query[0] == 1:
        #         obs.append(query[1])
        
        # obs.sort()
        # used = set()
        # ans = []

        # prev = 0
        # for i in range(len(queries)-1, -1, -1):
        #     if queries[i][0] == 1:
        #         used.add(queries[i][1])
        #     else:
        #         x = queries[i][1]
        #         sz = queries[i][2]
        #         prev = 0
        #         found = False
        #         for curr in obs:
        #             if curr >= x:
        #                 break
        #             if curr in used:
        #                 continue
        #             if curr - prev >= sz:
        #                 found = True
        #                 break
        #             prev = curr
        #         if not found:
        #             if x - prev >= sz:
        #                 found = True
        #         ans.append(found)
        # return ans[::-1]
        obs = []
        n = -1
        for query in queries:
            n = max(n, query[1])
            if query[0] == 1:
                obs.append(query[1])
        n += 1
        obs.sort()
        idx_mp = {}
        for idx, ob in enumerate(obs):
            idx_mp[ob] = idx
        
        seg = [0] * (4 * n)
        arr = [[-1, -1] for _ in range(n)]
        prev_obs = 0
        for i in range(len(obs)):
            prev = -1
            if i > 0:
                prev = obs[i-1]
            nxt = -1
            if i+1 < len(obs):
                nxt = obs[i+1]
            arr[obs[i]] = [prev, nxt]
        
        def build(i, l, r):
            if l == r:
                if l in idx_mp:
                    seg[i] = l - (arr[l][0] if arr[l][0] >= 0 else 0)
                return
            mid = (l + r) // 2
            build(2*i, l, mid)
            build(2*i + 1, mid+1, r)
            seg[i] = max(seg[2*i], seg[2*i +1])
            return
        build(1, 0, n - 1)

        def update(i,idx, l, r, val):
            if l == r == idx:
                prev = seg[i]
                seg[i] = val
                return prev
            mid = (l + r) // 2
            if idx <= mid:
                prev = update(2*i, idx, l, mid, val)
            else:
                prev = update(2*i + 1, idx, mid + 1,r, val)
            seg[i] = max(seg[2*i], seg[2*i +1])
            return prev
        
        def query(i, l, r, left, right):
            if left <= l and right >= r:
                return seg[i]
            if r < left or l > right:
                return 0
            mid = (l + r) // 2
            left_max = query(i*2, l, mid, left, right)
            right_max = query(i*2 + 1, mid+1, r, left, right)
            return max(left_max, right_max)
        
        ans = []
        active = SortedList(obs)
        for i in range(len(queries)-1, -1, -1):
            if queries[i][0] == 1:
                active.remove(queries[i][1])
                prev, nxt = arr[queries[i][1]]
                if prev != -1:
                    arr[prev][1] = nxt
                if nxt != -1:
                    arr[nxt][0] = prev
                update(1, queries[i][1], 0, n-1, 0)
                if nxt != -1:
                    update(1, nxt, 0, n-1, nxt - (prev if prev > 0 else 0))
            else:
                x = queries[i][1]
                sz = queries[i][2]
                mx = query(1, 0, n-1, 0, x)
                idx = active.bisect_right(x) - 1
                last_obs = 0 if idx < 0 else active[idx]
                if mx >= sz or (x - last_obs) >= sz:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans[::-1]

