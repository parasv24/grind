class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i , j = 0, 0
        mp = {}
        max_l = 0
        cur_l = 0
        og_k = k
        while j < len(nums):
            if nums[j] == 1:
                cur_l += 1
                max_l = max(max_l, cur_l)
                #print(j, nums[j], max_l, cur_l, k)
            else:
                if k > 0:
                    k -= 1
                    cur_l += 1
                    max_l = max(max_l, cur_l)
                else:
                    while cur_l > 0 and k <= 0:
                        if nums[i] == 0:
                            k += 1
                            k = min(k, og_k)
                        cur_l -= 1
                        i += 1
                    if k > 0:
                        cur_l += 1
                        k -= 1
                        max_l = max(max_l, cur_l)
                #print(j, nums[j], max_l, cur_l, k)
            j += 1
        return max_l