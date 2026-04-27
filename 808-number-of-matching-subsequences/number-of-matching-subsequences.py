class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # ans = 0
        # for word in words:
        #     i = 0
        #     j = 0
        #     while i < len(word) and j < len(s):
        #         if word[i] == s[j]:
        #             i += 1
        #             j += 1
        #         else:
        #             j += 1
        #     if i == len(word):
        #         ans += 1
        # return ans
        mp = defaultdict(list)
        for idx, ch in enumerate(s):
            mp[ch].append(idx)
        ans = 0
        # print(mp)
        for word in words:
            prev_idx = -1
            flag = True
            for ch in word:
                nxt_idx = bisect_left(mp[ch], prev_idx + 1)
                # print(word, ch, nxt_idx, prev_idx + 1)
                if nxt_idx == len(mp[ch]):
                    flag = False
                    break
                prev_idx = mp[ch][nxt_idx]
            ans += int(flag)
        return ans
            

