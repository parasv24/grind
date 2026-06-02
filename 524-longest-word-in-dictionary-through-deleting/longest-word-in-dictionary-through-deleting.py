class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            i = 0
            j = 0
            while i < len(word) and j < len(s):
                if s[j] == word[i]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(word):
                return word
        return ""