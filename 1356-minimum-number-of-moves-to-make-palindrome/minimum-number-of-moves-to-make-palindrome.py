class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:

        n = len(s)
        s = [ch for ch in s]

        def rec(i):

            if i >= n - i - 1:
                return 0

            j = n - i - 1

            idx1 = -1
            idx2 = -1

            for idx in range(i, j):
                if s[idx] == s[j]:
                    idx1 = idx
                    break

            for idx in range(j, i, -1):
                if s[idx] == s[i]:
                    idx2 = idx
                    break

            ans = 0

            if idx1 == -1:

                ans += j - idx2

                k = idx2

                while k < j:
                    s[k], s[k+1] = (
                        s[k+1],
                        s[k]
                    )
                    k += 1

            elif idx2 == -1:

                ans += idx1 - i

                k = idx1

                while k > i:
                    s[k], s[k-1] = (
                        s[k-1],
                        s[k]
                    )
                    k -= 1

            else:

                left_cost = idx1 - i
                right_cost = j - idx2

                if left_cost <= right_cost:

                    ans += left_cost

                    k = idx1

                    while k > i:
                        s[k], s[k-1] = (
                            s[k-1],
                            s[k]
                        )
                        k -= 1

                else:

                    ans += right_cost

                    k = idx2

                    while k < j:
                        s[k], s[k+1] = (
                            s[k+1],
                            s[k]
                        )
                        k += 1

            return ans + rec(i + 1)

        return rec(0)