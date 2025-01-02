class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ["a", "e", "i", "o", "u"]
        prefix_sums = []
        for i in range(len(words)):
            cur_i = int((words[i][0] in vowels and words[i][-1] in vowels))
            if i > 0:
                prefix_sums.append(prefix_sums[-1]  + cur_i)
            else:
                prefix_sums.append(cur_i)

        ans = []
        for x, y in queries:
            if x > 0 :
                ans.append(prefix_sums[y] - prefix_sums[x-1])
            else:
                ans.append(prefix_sums[y])    
        return ans
