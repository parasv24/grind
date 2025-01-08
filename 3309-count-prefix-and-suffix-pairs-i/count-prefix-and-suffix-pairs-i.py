class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                b , a = words[j], words[i]
                if len(words[i]) <= len(words[j]):
                    ans += int(a == b[: len(a)] and a == b[len(b) - len(a):])
        return ans