class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.logn = n.bit_length()
        self.lift_table = [[0 for _ in range(n)] for _ in range(self.logn)]
        for i in range(self.logn):
            for j in range(n):
                if i == 0:
                    self.lift_table[i][j] = parent[j]
                else:
                    val = self.lift_table[i-1][j]
                    if val != -1:
                        val = self.lift_table[i-1][val]
                    self.lift_table[i][j] = val
        # print(self.lift_table)
    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.logn):
            if k & (1 << i):
                if node != -1:
                    node = self.lift_table[i][node]
        return node


        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)