class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        i = 0
        ans = 1000
        while i < len(words):
            check_i = (startIndex + i) % len(words)
            if words[check_i] == target:
                ans = min(ans, abs(i), abs(len(words) - i))
            i += 1
        return ans if ans < 1000 else -1
            