class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        size = 2 * n + 1
        offset = n

        seg = [0] * (4 * size)

        def update(node, l, r, pos):
            if l == r:
                seg[node] += 1
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2 + 1, l, mid, pos)
            else:
                update(node * 2 + 2, mid + 1, r, pos)

            seg[node] = seg[node * 2 + 1] + seg[node * 2 + 2]

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return 0

            if ql <= l and r <= qr:
                return seg[node]

            mid = (l + r) // 2

            return (
                query(node * 2 + 1, l, mid, ql, qr)
                + query(node * 2 + 2, mid + 1, r, ql, qr)
            )

        prefix = 0
        ans = 0

        # insert prefix[0] = 0
        update(0, 0, size - 1, offset)

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            pos = prefix + offset

            if pos > 0:
                ans += query(0, 0, size - 1, 0, pos - 1)

            update(0, 0, size - 1, pos)

        return ans