class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        digits = 0
        sm = 0
        
        for ch in s:
            if ch != "0":
                digits = digits * 10 + int(ch)
                sm += int(ch)
        
        return digits * sm
