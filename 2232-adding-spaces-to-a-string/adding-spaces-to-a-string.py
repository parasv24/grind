class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        prev = 0
        output = ""
        for el in spaces:
            output += s[prev:el] + " "
            prev = el
        output += s[prev: ]
        return output
        