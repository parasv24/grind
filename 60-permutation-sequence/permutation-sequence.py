class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def perms(i):
            if i == n:
                return [str(n)]
            small_ans = perms(i+1)
            ans = []
            for string in small_ans:
                for idx in range(len(string)+1):
                    pre = string[0: idx] if idx > 0 else ""
                    cur = str(i)
                    suf = string[idx: ] if idx < len(string) else ""
                    ans.append(pre + cur + suf)
            return ans
        return sorted(perms(1))[k-1]

        