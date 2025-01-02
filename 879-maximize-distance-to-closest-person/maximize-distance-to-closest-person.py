class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left_1 = -1
        lefts = [1000000] * len(seats)
        for i in range(len(seats)):
            if seats[i] == 1:
                left_1 = i
            else:
                if left_1 != -1:
                    lefts[i]= i - left_1
        rights = [1000000] * len(seats)
        right_1 = -1
        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                right_1 = i
            else:
                if right_1 != -1:
                    rights[i] = right_1 - i
        ans = -1
        for i in range(len(seats)):
            if seats[i] == 0:
                ans = max(ans, min(lefts[i], rights[i]))
        return ans
            
        