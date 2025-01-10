class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mp = [[0] * len(words1) for _ in range(26)]
        for idx, word in enumerate(words1):
            for ch in word:
                mp[ord(ch) - ord('a')][idx] += 1
        final_mp = [0] * 26
        for idx, word in enumerate(words2):
            mp2 = [0] * 26
            for ch in word:
                mp2[ord(ch)- ord('a')] += 1
                final_mp[ord(ch)- ord('a')] = max(mp2[ord(ch)- ord('a')], final_mp[ord(ch)- ord('a')])
        ans = [1] * len(words1)
        for i in range(26):
            for idx, val in enumerate(mp[i]):
                if val < final_mp[i]:
                    ans[idx] = 0
        return [words1[idx] for idx in range(len(ans)) if ans[idx] == 1]

