class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        cnt = 0
        total_days = max(event[1] for event in events)
        day = 1
        event_id = 0
        min_heap = []
        while day <= total_days:
            if event_id < len(events) and not min_heap:
                day = events[event_id][0]
            
            while event_id < len(events) and events[event_id][0] <= day:
                heapq.heappush(min_heap, events[event_id][1])
                event_id += 1
            
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            if min_heap:
                heapq.heappop(min_heap)
                cnt += 1
            elif event_id >= len(events):
                break
            day += 1
        return cnt

        