class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        m = modulo
        arr = [int((el - k) % m == 0) for el in nums]
        #print(arr)
        mp = Counter({0:1})
        ans =0
        prev = 0
        for i in range(len(arr)):
            prev = (arr[i] + prev) % m
            ans += mp[(prev - k)%m]
            mp[prev] += 1
        return ans

        