class Solution:
    def minimumDistance(self, word: str) -> int:
        @cache
        def dist(a, b):
            if a is None:
                return 0
            ax, ay = divmod(a, 6)
            bx, by = divmod(b, 6)
            return abs(ax - bx) + abs(ay - by)

        @cache
        def solve(i, f1, f2):
            if i == len(word):
                return 0

            cur = ord(word[i]) - ord('A')

            # Option 1: use finger 1
            use_f1 = dist(f1, cur) + solve(i+1, cur, f2)

            # Option 2: use finger 2
            use_f2 = dist(f2, cur) + solve(i+1, f1, cur)

            return min(use_f1, use_f2)

        return solve(0, None, None)
