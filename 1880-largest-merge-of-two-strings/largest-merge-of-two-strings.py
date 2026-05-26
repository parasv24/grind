class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # @cache
        # def rec(i, j):
        #     if i == len(word1):
        #         if j < len(word2):
        #             return word2[j] + rec(i, j+1)
        #         else:
        #             return ""
            
        #     if j == len(word2):
        #         if i < len(word1):
        #             return word1[i] + rec(i+1, j)
        #         else:
        #             return ""
            
        #     ans1 = word1[i] + rec(i+1, j)
        #     ans2 = word2[j] + rec(i, j+1)
        #     if ans1 > ans2:
        #         return ans1
        #     else:
        #         return ans2
        # return rec(0, 0)

        i, j = 0, 0
        ans = []
        while i < len(word1) and j < len(word2):
            # print(i, j, ans)
            if word1[i] > word2[j]:
                ans.append(word1[i])
                i += 1
            elif word2[j] > word1[i]:
                ans.append(word2[j])
                j += 1
            else:
                pre_i = i
                pre_j = j
                while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                    i += 1
                    j += 1
                if i < len(word1) and j < len(word2):
                    if word1[i] > word2[j]:
                        ans.append(word1[pre_i])
                        i = pre_i + 1
                        j = pre_j
                    else:
                        ans.append(word2[pre_j])
                        i = pre_i
                        j = pre_j + 1
                elif i < len(word1):
                    ans.append(word1[pre_i])
                    i = pre_i + 1
                    j = pre_j
                else:
                    ans.append(word2[pre_j])
                    i = pre_i
                    j = pre_j + 1
        if i < len(word1):
            for k in range(i, len(word1)):
                ans.append(word1[k])
        if j < len(word2):
            for k in range(j, len(word2)):
                ans.append(word2[k])
        return "".join(ans)





