class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = [1 if (el & 1) else 0 for el in nums]
        prev = 0
        ans = 0
        mp = {}
        mp[0] = 1
        for i in range(0,len(arr)):
            prev += arr[i]
            ans += mp.get(prev - k,0)
            mp[prev] = mp.get(prev,0) + 1
        return ans

        

        