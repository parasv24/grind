class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        size = {chr(i): 1 for i in range(ord('a'), ord('z') + 1)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]
            return True
        for eq in equations:
            x, op, y = eq[0], eq[1:3], eq[-1]
            if op == "==":
                union(x, y)
        for eq in equations:
            x, op, y = eq[0], eq[1:3], eq[-1]
            if op == "!=":
                if find(x) == find(y):
                    return False
        return True