class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            sm = 0
            for ch in word:
                sm += weights[ord(ch) - ord('a')]
            sm %= 26
            ans.append(chr(ord('z') - sm))
        return "".join(ans)

        