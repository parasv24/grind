class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n= len(lcp)
        for i in range(n):
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if i == j and lcp[i][j] != n - i:
                    return ""
                if lcp[i][j] > n-i:
                    return ""
        idxs = [-1 for i in range(n)]
        k , k_used =0, False
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0 and idxs[j] == -1:
                    idxs[j] = chr(ord('a') + k)
                    k_used = True
            if k_used:
                k += 1
                k_used = False
                if k > 26:
                    return ""
        # print(idxs)
        word = "".join(idxs)
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j]:
                        return ""
                else:
                    if i == n-1 or j == n-1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i+1][j+1] + 1:
                            return ""
                
        return word
        