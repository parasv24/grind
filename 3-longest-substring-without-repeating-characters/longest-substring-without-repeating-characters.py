class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        maxi, i , j = 0 , 0 , 0
        
        while j < len(s):
            if mp.get(s[j], False) == False:
                mp[s[j]] = True
            else:
                maxi = max(maxi, j - i)
                while s[i] != s[j] and i < j:
                    mp[s[i]] = False
                    i += 1
                i += 1
            j += 1
        maxi = max(maxi, j - i)
        return maxi
            
        