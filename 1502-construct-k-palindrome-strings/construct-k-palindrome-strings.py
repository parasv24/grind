class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        mp = Counter(list(s))
        cnt = 0
        for _, value in mp.items():
            if value % 2 == 1:
                cnt += 1
                if cnt > k:
                    return False
        return True