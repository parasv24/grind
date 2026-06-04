class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        x= 0
        total = 0
        for i in range(101, num2+1):
            s = str(i)
            for j in range(1, len(s) - 1):
                if  s[j-1] < s[j] > s[j+1]:
                    total += 1
                if s[j-1] > s[j] < s[j+1]:
                    total += 1
            if i == num1 - 1:
                x = total
        return total - x
                
        