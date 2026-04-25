class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        evens = [0] * len(nums)
        for i in range(len(nums)):
            evens[i] = int(nums[i] % 2 == 0)
            if i > 0:
                evens[i] += evens[i-1]
        
        def get_count(val, left, right):
            # print("start_val", val)
            index = -1
            left_l = left
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] <= val:
                    index = middle
                    left = middle + 1
                else:
                    right = middle - 1
            if index >= 0:
                left_evens = 0
                if left_l > 0:
                    left_evens = evens[left_l - 1]
                val = val -  (2 * (evens[index] - left_evens))
            # print("end_val", val, index, evens)
            return val // 2

        ans = []
        for l, r, k in queries:
            ele = k * 2
            idx = -1
            start , end = ele, ele + (2 * (r - l + 1))
            # print("start", l, r, k , start, end, idx)
            while start <= end:
                mid = (start + end) // 2      
                if mid % 2 != 0:
                    mid -= 1
                if get_count(mid, l, r) >= k:
                    idx = mid
                    end = mid - 2
                else:
                    start = mid + 2
            # print("end", l, r, k , start, end, idx)
            ans.append(idx)
        return ans
            