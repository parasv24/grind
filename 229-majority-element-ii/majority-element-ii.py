class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1, cnt2 = 0 , 0
        el1, el2 = 0, 0

        for el in nums:
            if cnt1 == 0 and el != el2:
                cnt1 = 1
                el1 = el
            elif cnt2 == 0 and el!= el1:
                cnt2 = 1
                el2 = el
            elif el == el1:
                cnt1 += 1
            elif el == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        exp_cnt = (len(nums) // 3) + 1
        cnt1, cnt2 = 0, 0
        for el in nums:
            if el == el1:
                cnt1 += 1
            elif el == el2:
                cnt2 += 1
        ans = []
        # print(cnt1, el1, cnt2, el2)
        if cnt1 >= exp_cnt:
            ans.append(el1)
        if cnt2 >= exp_cnt:
            ans.append(el2)
        return ans





