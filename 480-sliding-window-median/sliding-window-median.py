class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        i, j = 0, 0
        mx_heap = []
        min_heap = []
        len_mx = 0
        len_min = 0
        while j < len(nums):
            heappush(mx_heap, [-nums[j], -j])
            len_mx += 1
            if len_mx > len_min + 1:
                tup = heappop(mx_heap)
                tup = [x * -1 for x in tup]
                heappush(min_heap, tup)
                len_mx -= 1
                len_min += 1
            if mx_heap:
                tup1 = heappop(mx_heap)
                tup1 = [x * -1 for x in tup1]
                heappush(min_heap, tup1)
                tup2 = heappop(min_heap)
                tup2 = [x * -1 for x in tup2]
                heappush(mx_heap, tup2)
            # print(mx_heap, min_heap, len_mx, len_min)
            if j - i == k - 1:
                while mx_heap and -mx_heap[0][1] < i:
                    heappop(mx_heap)
                while min_heap and min_heap[0][1] < i:
                    heappop(min_heap)
                
                if k % 2 != 0:
                    ans.append(-mx_heap[0][0])
                else:
                    ans.append((-mx_heap[0][0] + min_heap[0][0])/ 2)
                    
                if nums[i] <= -mx_heap[0][0]:
                    len_mx -= 1
                    if len_mx < len_min:
                        tup = heappop(min_heap)
                        tup = [x * -1 for x in tup]
                        heappush(mx_heap, tup)
                        len_mx += 1
                        len_min -= 1
                else:
                    len_min -= 1
                    if len_mx > len_min + 1:
                        tup = heappop(mx_heap)
                        tup = [x * -1 for x in tup]
                        heappush(min_heap, tup)
                        len_mx -= 1
                        len_min += 1
                i += 1
            # print(mx_heap, min_heap, len_mx, len_min)
            # print(ans)
            j += 1
        return ans