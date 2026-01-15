class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts = [0] * len(height) 
        max_rights = [0] * len(height)
        stck = []
        for idx in range(0, len(height)):
            if len(stck) != 0:
                while len(stck) > 0 and stck[-1] <= height[idx]:
                    stck.pop()
                if len(stck) > 0:
                    max_lefts[idx] = stck[-1]
                if len(stck) == 0 or stck[-1] < height[idx]:
                    stck.append(height[idx])
            else:
                stck.append(height[idx])
        stck = []
        for idx in range(len(height)-1, -1, -1):
            if len(stck) != 0:
                while len(stck) > 0 and stck[-1] <= height[idx]:
                    stck.pop()
                if len(stck) > 0:
                    max_rights[idx] = stck[-1]
                if len(stck) == 0 or stck[-1] < height[idx]:
                    stck.append(height[idx])
            else:
                stck.append(height[idx])
        ans = 0
        # print(max_lefts, max_rights)
        for i in range(0, len(height)):
            mini = min(max_lefts[i], max_rights[i])
            print(max_lefts[i], max_rights[i], height[i])
            if height[i] < mini:
                ans += mini - height[i]
                print(i, ans)
        return ans
        
                

