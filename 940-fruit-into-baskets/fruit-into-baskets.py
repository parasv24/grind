class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = set()
        mp = Counter()
        maxi, i, j = 0, 0 , 0
        while j < len(fruits):
            baskets.add(fruits[j])
            mp[fruits[j]] += 1
            if len(baskets) > 2:
                while len(baskets) > 2:
                    mp[fruits[i]] -= 1
                    if mp[fruits[i]] == 0:
                        baskets.remove(fruits[i])
                    i += 1
            maxi = max(maxi, j - i + 1)
            j += 1
        return maxi
                        