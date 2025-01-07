class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mp = Counter({})
        for el in arr:
            el = el % k
            #print(k-el)
            if mp[(k-el)%k] > 0:
                mp[(k-el)%k] -= 1
            else:
                mp[el] += 1
        print(mp)
        return sum(mp.values()) == 0
        