class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = [1000000] * 10001
        for st, end in intervals:
            if mp[st] == 1000000:
                mp[st] = 0
            if mp[end] == 1000000:
                mp[end] = 0
            mp[st] += 1
            mp[end]-= 1
        ans = []
        i , prev = 0, 0
        # print(mp)
        while i < 10001:
            if mp[i] != 1000000:
                start = i
                sm = mp[i]
                while sm >= 0 and i < 10001:
                    if sm == 0:
                        ans.append([start, i])
                        break
                    i += 1
                    if mp[i] != 1000000:
                        sm += mp[i]
            i += 1
        return ans

        
        