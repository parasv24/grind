class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # O( n log n)
        # cnt_t = Counter(t)
        # print(cnt_t)
        # def get_string(k):
        #     i = 0
        #     j = 0
        #     mp = defaultdict(int)
        #     while j < len(s):
        #         mp[s[j]] += 1
        #         if j - i == k - 1:
        #             keys = 0
        #             for key in cnt_t.keys():
        #                 if cnt_t[key] <= mp[key]:
        #                     keys += 1
        #             if keys == len(cnt_t.keys()):
        #                 return s[i:j+1]
        #             mp[s[i]] -= 1
        #             i += 1
        #         j += 1
            
        #     return ""

        # l , r = len(t), len(s)
        # ans = ""
        # while l <= r:
        #     mid = (l + r) // 2
        #     string = get_string(mid)
        #     if string != "":
        #         ans = string
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return ans

        cnt_t = Counter(t)
        i , j = 0, 0
        mp = defaultdict(int)
        keys = 0
        ans = (-1, -1)
        length = 1000000
        while j < len(s):
            mp[s[j]] += 1
            if s[j] in cnt_t and mp[s[j]] == cnt_t[s[j]]:
                keys += 1
            # print(i, j, keys, len(cnt_t.keys()))
            while keys == len(cnt_t.keys()):
                if j - i < length:
                    ans = (i, j)
                    length = j - i
                if s[i] in cnt_t and mp[s[i]] == cnt_t[s[i]]:
                    keys -= 1
                mp[s[i]] -= 1
                i += 1
            j += 1
        # print(ans)
        return s[ans[0]: ans[1] + 1] if ans != (-1, -1) else ""
        