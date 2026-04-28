class Solution:
    def reverse(self, x: int) -> int:
        is_neg = -1 if x < 0 else 1
        bound = pow(2, 31)
        x = abs(x)
        num = 0
        while x > 0:
            num = num * 10 +  x % 10
            x = x // 10
        num *= is_neg
        return num if -bound <= num <= bound -1 else 0
        


        