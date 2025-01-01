class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        mp = {}
        for x , y in intervals:
            mp[x] = mp.get(x, 0) + 1
            mp[y] = mp.get(y, 0) - 1
        x,y = newInterval
        mp[x] = mp.get(x, 0) + 1
        mp[y] = mp.get(y, 0) - 1
        ans = []
        temp = []
        prev = 0
        for key in sorted(mp.keys()):
            if prev == 0:
                temp.append(key)
            mp[key] += prev
            prev = mp[key]
            if mp[key] == 0:
                temp.append(key)
                ans.append(temp)
                temp = []
        # print(mp)
        return ans


        