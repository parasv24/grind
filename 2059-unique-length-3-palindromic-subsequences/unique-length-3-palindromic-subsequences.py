class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mp = [[-1,-1] for _ in range(26)]
        cnt = [[0] * 26] * len(s)
        for i in range(len(s)):
            idx = ord(s[i]) - 97
            if mp[idx][0] == -1:
                mp[idx][0] = i
            if mp[idx][1] < i:
                mp[idx][1] = i
            if i == 0:
                cnt[i][idx] += 1
            else:
                cnt[i] = cnt[i-1][:]
                cnt[i][idx] += 1
        ans = 0
        #print(mp)
        for i in range(26):
            if mp[i][0] in [mp[i][1], mp[i][1] + 1] :
                continue
            l ,r = mp[i]
            #print(l , r, i)
            for j in range(26):
                count = cnt[r][j] - cnt[l][j]
                if (i == j and count >= 2) or (i != j and count >= 1):
                    ans += 1

        return ans