class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mp = {}
        mini = 10 ** 9
        def rev(el):
            new = 0
            while el:
                new = new * 10 + el % 10
                el = el // 10
            return new

        for i, el in enumerate(nums):
            # print(rev(el), el, mp)
            idx = mp.get(el, -1)
            mp[rev(el)] = i
            if idx != -1 and i != idx:
                # print(i, idx)
                mini = min(mini, i - idx)
        return mini if mini < 10 **9 else -1

        # l, r = 1 , len(nums) - 1
        # ans = -1
        # while l <= r:
        #     mid = (l+r)//2
        #     if is_poss(mid)


        