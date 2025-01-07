class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        prev = 0
        div = []
        for el in word:
            prev = (prev * 10 + int(el)) % m
            div.append(int(prev == 0))
        return div
        