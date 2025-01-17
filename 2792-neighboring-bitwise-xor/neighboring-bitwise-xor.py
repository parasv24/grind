class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor = 0
        for el in derived:
            xor ^= el
        return xor == 0
        