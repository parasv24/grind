class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        arr = [(positions[i], healths[i], directions[i], i) for i in range(len(positions))]
        arr.sort()
        stck = []
        ans = []
        for i in range(len(arr)):
            pos, h, d, idx = arr[i]
            if d == "R":
                stck.append((h, idx))
            if d == "L":
                while len(stck) > 0:
                    h2, idx2 = stck .pop()
                    if h2 > h:
                        h = 0
                        stck.append((h2-1, idx2))
                        break
                    elif h2 == h:
                        h = 0
                        break
                    else:
                        h -= 1
                if h > 0:
                    ans.append((h, idx))
        ans += stck
        ans.sort(key=lambda x: x[1])
        return [ans[i][0] for i in range(len(ans))]