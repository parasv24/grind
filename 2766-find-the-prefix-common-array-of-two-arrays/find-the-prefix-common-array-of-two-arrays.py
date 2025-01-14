class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        arr = [[0,0] for _ in range(len(A))]
        ans = []
        prev = 0
        for x, y in zip(A, B):
            arr[x-1][0] += 1
            arr[y-1][1] += 1
            if x == y:
                prev = prev + 1
            else:
                prev += int(arr[x-1][0]>0 and arr[x-1][1] > 0) + int(arr[y-1][0]>0 and arr[y-1][1] > 0)
            ans.append(prev)
        return ans

        