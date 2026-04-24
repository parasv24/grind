class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[position[i], speed[i]] for i in range(len(position))]
        arr.sort(key= lambda x: -x[0])
        fleets = 1
        prev_time_taken = (target - arr[0][0]) / (arr[0][1] * 1.0)
        for i in range(1, len(arr)):
            time_taken = (target - arr[i][0]) / (arr[i][1] * 1.0)
            if prev_time_taken < time_taken:
                fleets += 1
                prev_time_taken = time_taken
        return fleets