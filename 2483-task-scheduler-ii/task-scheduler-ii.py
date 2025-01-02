class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        i = 0
        time = 0
        mp = {}
        while i < len(tasks):
            time += 1
            if mp.get(tasks[i], 1) <= time:
                #print(time, tasks[i], i, mp.get(tasks[i], 1))
                mp[tasks[i]] = time + space + 1
                i += 1
            else:
                time = mp.get(tasks[i], 1) - 1
        return time