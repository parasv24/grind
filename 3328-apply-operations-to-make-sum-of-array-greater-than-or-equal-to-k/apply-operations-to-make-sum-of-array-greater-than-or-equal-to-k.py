class Solution:
    def minOperations(self, k: int) -> int:
        if k == 1:
            return 0
        
        num = int(sqrt(k))
        val = ((k-1) // num) + 1
        return val + num - 1 - 1
        