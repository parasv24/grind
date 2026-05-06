class Solution:
    def candy(self, ratings: List[int]) -> int:
        idxs = defaultdict(list)
        candies = [0] * len(ratings)
        for i in range(len(ratings)):
            idxs[ratings[i]].append(i)
        for key in sorted(idxs.keys()):
            mp = {}
            for value in idxs[key]:
                val = 1
                if value > 0 and candies[value - 1] != 0:
                    val = max(val, candies[value -1] + 1)
                if value < len(candies) - 1 and candies[value + 1] != 0:
                    val = max(val, candies[value + 1] + 1)
                mp[value] = val
            for k in mp.keys():
                candies[k] = mp[k]
        return sum(candies)
        

        