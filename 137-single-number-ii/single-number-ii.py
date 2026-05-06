class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        negative = [0] * 32
        positive = [0] * 32
        for el in nums:
            if el < 0:
                rep = bin(abs(el))[2:][::-1]
                for i in range(len(rep)):
                    negative[i] += int(rep[i])
            else:
                rep = bin(abs(el))[2:][::-1]
                for i in range(len(rep)):
                    positive[i] += int(rep[i])
        ans = 0
        # print(positive, negative)
        for i in range(32):
            if positive[i] % 3 != 0:
                ans += pow(2, i)
        if ans > 0:
            return ans
        for i in range(32):
            if negative[i] % 3 != 0:
                ans += pow(2, i)
        if ans > 0:
            return -ans
        return ans


        