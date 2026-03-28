class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def rec(i, prev, arr):
            if i == len(s):
                if prev == len(s) - 1:
                    ans.append(arr)
                return
            cur = s[prev+1: i+1]
            if cur == cur[::-1]:
                rec(i+1, i, arr + [cur])
            rec(i+1, prev, arr)
        rec(0, -1, [])
        return ans
        
            
            
        

        