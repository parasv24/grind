class Solution:
    def minimumPushes(self, word: str) -> int:
        mp = Counter(word)
        tup = [(v, k) for k,v in mp.items()]
        tup.sort(reverse=True)
        val = 2
        cycle = 1
        new_mp = {}
        for _, k in tup:
            new_mp[k] = cycle
            if val == 9:
                val = 1
                cycle += 1
            val += 1
        print(new_mp)
        ans = 0
        for w in word:
            ans += new_mp[w]
            # print(w, new_mp[w])
        return ans

