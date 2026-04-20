class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i , j = 0 , 0
        values = []
        while j < len(s):
            if j - i == 9:
                values.append(s[i: j+1])
                i += 1
            j += 1
        return [k for k, v in Counter(values).items() if v >= 2]

        