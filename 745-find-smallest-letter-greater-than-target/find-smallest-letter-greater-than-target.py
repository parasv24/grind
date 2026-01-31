class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = "zz"
        for el in letters:
            if target < el and el < ans:
                ans = el
        return ans if ans != "zz" else letters[0]
        