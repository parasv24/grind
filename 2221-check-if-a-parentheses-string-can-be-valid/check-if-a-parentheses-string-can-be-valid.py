class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        openb = []
        unlocked = []
        for i in range(len(s)):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                openb.append(i)
            else:
                if len(openb) > 0:
                    openb.pop()
                elif len(unlocked) > 0:
                    unlocked.pop()
                else:
                    return False
        while openb and unlocked and openb[-1] < unlocked[-1]:
            openb.pop()
            unlocked.pop()
        if openb or (len(unlocked) % 2 == 1):
            return False
        return True
            