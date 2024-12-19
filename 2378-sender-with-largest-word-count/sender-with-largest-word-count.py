class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        mp = {}
        for idx, key in enumerate(senders):
            mp[key] = mp.get(key,0) + len(messages[idx].split(" "))
        cnt = -1
        ans  = ""
        # print(mp)
        for key in mp.keys():
            if mp[key] > cnt:
                cnt = mp[key]
                ans = key
            if mp[key] == cnt:
                ans = max(ans, key)
        return ans