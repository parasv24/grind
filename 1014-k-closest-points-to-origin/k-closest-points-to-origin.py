class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mx_heap = []
        for i in range(len(points)):
            x, y = points[i]
            heappush(mx_heap, [-(x*x + y * y), x, y])
            if len(mx_heap) > k:
                heappop(mx_heap)
        return [[x, y] for _, x, y in mx_heap]
        