class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = [-1 * a, -1 * b,-1 *c]
        heapify(arr)
        moves= 0
        while len(arr) > 1:
            x = heappop(arr)
            y = heappop(arr)
            x+= 1
            y+=1
            moves+=1
            if x < 0:
                heappush(arr, x)
            if y < 0:
                heappush(arr, y)
        return moves