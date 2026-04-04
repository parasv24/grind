class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        diagonals = defaultdict(list)
        k = 0
        for i in range(rows):
            for j in range(cols):
                diagonals[j - i].append(encodedText[k])
                k += 1
        ans = []
        for i in range(cols):
            ans += diagonals[i]
        return "".join(ans).rstrip()
        