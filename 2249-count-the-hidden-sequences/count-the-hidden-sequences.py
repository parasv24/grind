class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        sm = 0
        mini = 0
        maxi = 0
        for i in differences:
            sm += i
            mini = min(mini,sm)
            maxi = max(maxi, sm)
        new_range = [lower + abs(mini), upper - maxi]
        #print(mini , maxi)
        ans = new_range[1] - new_range[0] + 1
        return ans if ans >=0 else 0
        