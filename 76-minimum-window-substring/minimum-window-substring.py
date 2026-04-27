class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        print(cnt_t)
        def get_string(k):
            i = 0
            j = 0
            mp = defaultdict(int)
            while j < len(s):
                mp[s[j]] += 1
                if j - i == k - 1:
                    keys = 0
                    for key in cnt_t.keys():
                        if cnt_t[key] <= mp[key]:
                            keys += 1
                    if keys == len(cnt_t.keys()):
                        return s[i:j+1]
                    mp[s[i]] -= 1
                    i += 1
                j += 1
            
            return ""

        l , r = len(t), len(s)
        ans = ""
        while l <= r:
            mid = (l + r) // 2
            string = get_string(mid)
            if string != "":
                ans = string
                r = mid - 1
            else:
                l = mid + 1
        return ans