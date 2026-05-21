class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        class TrieNode:
            def __init__(self, is_end=False):
                self.children = [0] * 10
                self.is_end = is_end

        root = TrieNode()

        def get_digits(num):
            ans = []
            while num:
                ans.append(num % 10)
                num = num // 10
            return ans

        for num in arr1:
            curr = root
            digits = get_digits(num)
            for i in range(len(digits) - 1, -1, -1):
                if curr.children[digits[i]] == 0:
                    curr.children[digits[i]] = TrieNode()
                curr = curr.children[digits[i]]
            curr.is_end = True
        ans = 0
        for num in arr2:
            curr = root
            digits = get_digits(num)
            print(digits)
            length = 0
            for i in range(len(digits) - 1, -1, -1):
                if curr.children[digits[i]] != 0:
                    length += 1
                    curr = curr.children[digits[i]]
                else:
                    break
            ans = max(ans, length)
        return ans


        