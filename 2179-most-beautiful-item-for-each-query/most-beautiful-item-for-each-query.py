class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda item: (item[0], -item[1]))
        max_till_now = -1
        for i in range(0, len(items)):
            if max_till_now > items[i][1]:
                items[i][1] = max_till_now
            else:
                max_till_now = items[i][1]
        ans_idx = []
        queries = [[query, idx] for idx, query in enumerate(queries)]
        queries.sort(key=lambda item: item[0])
        i = 0
        for query in queries:
            while items[i][0] < query[0] and i!= len(items) - 1:
                i += 1
            if items[i][0] > query[0] and i == 0:
                ans = 0
            elif items[i][0] > query[0]:
                ans = items[i-1][1]
            else:
                ans = items[i][1]
            ans_idx.append([ans,query[1]])
        ans_idx.sort(key=lambda item: item[1])
        ans = [x for x, y in ans_idx]
        return ans

        