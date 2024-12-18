class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        mx = -1
        for i in range(len(processorTime)):
            max_l = len(tasks) - 1 - (i * 4)
            for j in range(max_l, max_l - 4, -1):
                mx = max(mx, processorTime[i] + tasks[j])
        return mx
            

        