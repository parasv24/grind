class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            flag = False
            if n % 2 == 0:
                flag = True
                n = n // 2
            elif n % 3 == 0:
                flag = True
                n = n // 3
            elif n % 5 == 0:
                flag = True
                n = n // 5
            else:
                return False
        return True
        