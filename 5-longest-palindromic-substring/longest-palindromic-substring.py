class Solution:
    def longestPalindrome(self, s: str) -> str:
        @cache
        def rec(i):
            if i == len(s):
                return ""
            
            ans = ""
            for j in range(i+1, len(s)+1):
                string = s[i:j]
                if string == string[::-1]:
                    if len(string) > len(ans):
                        ans= string
                    small_ans = ""
                    if len(string) < len(s) + 1 - j:
                        small_ans = rec(j)
                    if len(small_ans) > len(ans):
                        ans = small_ans
            skip_ans = rec(i+1)
            return ans if len(ans) > len(skip_ans) else skip_ans
        return rec(0)
                        
                    
        