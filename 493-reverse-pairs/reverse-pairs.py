class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(start ,end):
            if start >= end:
                return 0
            mid = (start + end) // 2
            ans = 0
            ans += merge_sort(start, mid)
            ans += merge_sort(mid+1, end)
            i = start
            j = mid + 1
            length = end - start + 1
            temp = [0] * length
            # temp2 = [0] * length
            # k2 = 0
            k = 0
            while k < length:
                if i > mid:
                    temp[k] = nums[j]
                    j += 1
                elif j > end:
                    temp[k] = nums[i]
                    i += 1
                elif nums[i] <= 2* nums[j]:
                    temp[k] = nums[i]
                    i+= 1
                else:
                    temp[k] = nums[j]
                    j += 1
                    ans += (mid - i + 1)
                k += 1
            
            i = start
            j = mid + 1
            k = 0
            while k < length:
                if i > mid:
                    temp[k] = nums[j]
                    j += 1
                elif j > end:
                    temp[k] = nums[i]
                    i += 1
                elif nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i+= 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1
            for k in range(length):
                nums[start + k] = temp[k]
            return ans
        return merge_sort(0, len(nums) - 1)

        