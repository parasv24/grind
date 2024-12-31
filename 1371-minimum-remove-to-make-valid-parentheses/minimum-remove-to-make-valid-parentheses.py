class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stck = []
        output = ""
        removals = []
        for idx, el in enumerate(s):
            if el == "(":
                stck.append([el , idx])
            elif el == ")":
                if len(stck) > 0 and stck[-1][0] == "(":
                    stck.pop(-1)
                else:
                    removals.append(idx)
        for x, idx in stck:
            removals.append(idx)
        j = 0
        if len(removals) == 0:
            return s
        for idx, el in enumerate(s):
            if j < len(removals) and removals[j] == idx:
                j += 1
            else:
                output += el
        return output
            