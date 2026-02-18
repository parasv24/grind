class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        rep = bin(n)[2:]
        prev = rep[0]
        for el in rep[1:]:
            if el == prev:
                return False
            prev = el 
        return True
        