class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        line = [0] * (2 * limit + 2)
        i , j = 0, len(nums) - 1
        while i < j:
            x = nums[i]
            y = nums[j]
            x , y = min(x, y), max(x, y)
            if x != 1:
                line[2] += 2
                line[x + 1] -= 2
            line[x+1] += 1
            line[y+limit+1] -= 1
            if y != limit:
                line[y+limit+1] += 2
                line[limit+limit+1] -= 2
            i += 1
            j -= 1
        for i in range(2, 2*limit+2):
            line[i] += line[i-1]
        
        i , j = 0, len(nums) - 1
        while i < j:
            line[nums[i] + nums[j]] -= 1
            i += 1
            j -= 1
        line.pop()
        # print(line)
        return min(line[2:])
        
        