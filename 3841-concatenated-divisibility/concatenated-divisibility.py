class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
            nums.sort()
            @cache
            def rec(mask, rem):
                if mask == (1 << len(nums)) - 1:
                    return (rem == 0, [])
                ans = False
                for i in range(len(nums)):
                    if mask & (1 << i) == 0:
                        new_rem = int(str(rem) + str(nums[i])) % k
                        poss, ans = rec((1 << i) | mask, new_rem)
                        if poss:
                            ans.append(nums[i])
                            return True, ans
                return False, []
            _, ans = rec(0, 0)
            return ans[::-1]