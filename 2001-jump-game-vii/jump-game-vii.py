class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # if s[-1] == "1":
        #     return False
        # @cache
        # def rec(i):
        #     if i == len(s) - 1:
        #         return True
        #     flag = False
        #     for j in range(i + maxJump, i+minJump-1, -1):
        #         if j < len(s) and s[j] == "0":
        #             flag = flag or rec(j)
        #             if flag:
        #                 return flag
        #     return flag
        # return rec(0)
        pre = [0] * (len(s) + 1)
        pre[0] = 1
        pre[1] -=1

        for i in range(len(s)):
            if i > 0:
                pre[i] = pre[i] + pre[i-1]
            
            if pre[i] > 0 and s[i] == "0":
                j = min(i + maxJump+1, len(s))
                if i + minJump < len(s):
                    pre[i+minJump] += 1
                    pre[j] -= 1
        return pre[len(s)-1] > 0 and s[-1] == '0'

        

        