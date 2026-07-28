class Solution:
    def smallestPalindrome(self, s: str) -> str:
        mp = Counter(s)
        odd = ""
        ans = []
        for key in sorted(mp.keys()):
            if mp[key] % 2 == 1:
                odd = key
            ans += ([key] * (mp[key] // 2))
        string = "".join(ans)
        return string + odd + string[::-1]
        
        
            


        