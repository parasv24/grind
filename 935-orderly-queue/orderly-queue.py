class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            l = -1
            mini = "z" * len(s)
            for i in range(26):
                for j in range(len(s)):
                    if s[j] == chr(ord('a') + i):
                        mini = min(mini, s[j:] + s[:j])
                        l = 1
                if l != -1:
                    break
            return mini
        else:
            return "".join(sorted(s))

        