class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = [[capital[i], profits[i]] for i in range(len(capital))]
        arr.sort(key=lambda x: [x[0], -x[1]])
        # print(arr)
        i = 0
        hp = []
        while i < len(arr) and arr[i][0] <= w:
            hp.append(-(arr[i][1]))
            i += 1
        heapq.heapify(hp)
        ans = w
        # print(hp)
        while k > 0 and hp:
            ans += (-heapq.heappop(hp))
            # print(ans)
            while i < len(arr) and arr[i][0] <= ans:
                heapq.heappush(hp, -(arr[i][1]))
                i += 1
            k -= 1
        return ans