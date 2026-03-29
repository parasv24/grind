class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return ("".join(sorted([s1[0], s1[2]])) == "".join(sorted([s2[0], s2[2]]))) and ("".join(sorted([s1[1], s1[3]])) == "".join(sorted([s2[1], s2[3]])))
        
        