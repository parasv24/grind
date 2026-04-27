class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # combined = goal + "#" + s + s
        # lps = [0] * len(goal)
        # length = 0
        # i = 1
        # while i < len(combined):
        #     if combined[i] == combined[length]:
        #         length += 1
        #         if i < len(goal):
        #             lps[i] = length
        #         i += 1
        #     else:
        #         if length != 0:
        #             length = lps[length-1]
        #         else:
        #             i += 1
        #     if length == len(goal) and length == len(s) and i > len(goal):
        #         return True
        # return False
        if len(s) != len(goal):
            return False
        
        combined = goal + "#" + s
        lps = [0] * len(goal)
        length = 0
        i = 1
        while i < len(combined):
            if combined[i] == combined[length]:
                length += 1
                if i < len(goal):
                    lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length -1]
                else:
                    i += 1
        idx = len(s) - length
        combined = s[idx:] + s[:idx]
        # print(combined, idx, length)
        return combined == goal
        