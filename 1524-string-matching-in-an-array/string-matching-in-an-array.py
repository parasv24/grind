class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    ans.append(word)
                    break
        return ans


        