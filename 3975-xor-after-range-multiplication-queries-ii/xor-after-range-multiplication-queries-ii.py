class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        T = int(n**0.5)

        groups = [[] for _ in range(T)]
        for l,r,k,v in queries:
            if k < T:
                groups[k].append((l,r,v))
            else:
                for j in range(l, r+1, k):
                    nums[j] = (nums[j] * v) % mod
        
        for k in range(1, T):
            if not groups[k]:
                continue
            diff = [1] * (n + k)
            for l, r, v in groups[k]:
                diff[l] = (diff[l] * v) % mod
                R = ((r - l) // k) * k + l 
                diff[R+k] = (diff[R+k] * pow(v, mod-2, mod)) % mod
            
            for i in range(k, n):
                diff[i] = (diff[i] * diff[i-k]) % mod
            
            for i in range(n):
                nums[i] = (nums[i] * diff[i]) % mod
        res = 0
        for x in nums:
            res ^= x
        return res