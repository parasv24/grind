class Solution:
    def countMajoritySubarrays(self, nums, target):
        pre = [0]
        cur = 0
        for el in nums:
            x = 1 if el == target else -1
            cur += x
            pre.append(cur)
        
        def merge_sort(l, r):
            if l == r:
                return [pre[l]], 0
            mid = (l + r) // 2
            left_arr, left_ans = merge_sort(l , mid)
            right_arr, right_ans = merge_sort(mid+1, r)

            i = 0
            count = left_ans + right_ans
            for x in right_arr:
                while i < len(left_arr) and left_arr[i] < x:
                    i += 1
                count += i
            
            i , j = 0, 0
            combined_arr = []
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    combined_arr.append(left_arr[i])
                    i += 1
                else:
                    combined_arr.append(right_arr[j])
                    j += 1
            combined_arr.extend(left_arr[i:])
            combined_arr.extend(right_arr[j:])
            return combined_arr, count
        _, ans = merge_sort(0, len(pre)-1)
        return ans