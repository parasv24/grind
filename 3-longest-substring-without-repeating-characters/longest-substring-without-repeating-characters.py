class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i , j = 0, 0
        mp = {}
        max_l = 0
        cur_l = 0
        while j < len(s):
            if not mp.get(s[j], False):
                #print("if", j, max_l, cur_l, mp)
                mp[s[j]] = True
                cur_l += 1
                max_l = max(max_l, cur_l)
            else:
                #print("else", j, max_l, cur_l, mp)
                while cur_l > 0 and mp.get(s[j], False) == True:
                    mp[s[i]] = False
                    cur_l -= 1
                    i += 1
                mp[s[j]] = True
                cur_l += 1
                max_l = max(max_l, cur_l)
            j += 1
        return max_l
        