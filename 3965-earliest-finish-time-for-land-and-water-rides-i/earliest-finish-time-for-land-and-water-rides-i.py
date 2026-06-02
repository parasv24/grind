class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        mini = 10000
        val1 = -1
        duration1 = -1
        for ride, duration in zip(landStartTime, landDuration):
            if ride + duration < mini:
                mini = ride + duration
                val1 = ride
                duration1 = duration
        
        mini = 10000
        val2 = -1
        duration2 = -1
        ans = 20000
        time = val1 + duration1
        for ride, duration in zip(waterStartTime, waterDuration):
            if ride + duration < mini:
                mini = ride + duration
                val2 = ride
                duration2 = duration
            if time > ride:
                ans = min(ans, time + duration)
            else:
                ans = min(ans, ride + duration)
            
        time = val2 + duration2
        for ride, duration in zip(landStartTime, landDuration):
            if time > ride:
                ans = min(ans, time + duration)
            else:
                ans = min(ans, ride + duration)
        return ans    