class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class Node:
            def __init__(self, val = 0):
                # will be 2 only
                self.children = {}
        
        root = Node()
        maxima = 0
        for num in nums:
            curr = root
            bi = bin(num)[2:].zfill(32)
            for i in range(0, 32):
                if bi[i] not in curr.children:
                    curr.children[bi[i]] = Node()
                curr = curr.children[bi[i]]
            
            curr = root
            ans = 0
            ops = {"0": "1", "1": "0"}
            for i in range(0, 32):
                if ops[bi[i]] in curr.children:
                    curr = curr.children[ops[bi[i]]]
                    ans += pow(2, 31 - i)
                else:
                    curr = curr.children[bi[i]]
            maxima = max(maxima, ans)
        return maxima




