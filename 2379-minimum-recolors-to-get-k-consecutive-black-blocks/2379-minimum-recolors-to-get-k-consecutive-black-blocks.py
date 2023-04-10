class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        j = 0
        ans = k
        count = 0
        while (j < len(blocks)):
            if blocks[j] == 'W':
                count += 1
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                ans = min(ans, count)
                if blocks[i] == 'W':
                    count -= 1
                i += 1
                j += 1
        return ans
        