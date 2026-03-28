class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def rec(i, cur, arr):
            if i == len(s):
                if cur == "":
                    ans.append(arr)
                return
            cur += s[i]
            if cur == cur[::-1]:
                rec(i+1, "", arr + [cur])
            rec(i+1, cur, arr)
        rec(0, "", [])
        return ans
        
            
            
        

        