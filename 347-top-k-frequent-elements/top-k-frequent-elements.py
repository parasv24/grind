class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        arr = []
        for key, val in mp.items():
            if len(arr) < k:
                heappush(arr, (val, key))
            else:
                if arr[0][0] < val:
                    arr[0] = (val, key)
                    heapreplace(arr, (val, key))
        return [k for v ,k in arr]
        