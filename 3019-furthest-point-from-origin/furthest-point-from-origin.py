class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        total = 0
        dashes = 0
        for ch in moves:
            if ch == "L":
                total += -1
            elif ch == "R":
                total += 1
            else:
                dashes += 1
        return abs(total) + dashes
        