class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        tup = [[wordsContainer[i], i] for i in range(len(wordsContainer))]
        tup.sort(key= lambda x: len(x[0]))
        
        class Node:
            def __init__(self, val):
                self.val = val
                self.children = {}
        root = Node(tup[0][1])
        for word, idx in tup:
            curr = root
            for i in range(len(word)-1, -1, -1):
                ch = word[i]
                if ch not in curr.children:
                    curr.children[ch] = Node(idx)
                curr = curr.children[ch]
        ans = []
        for word in wordsQuery:
            curr = root
            for i in range(len(word)-1, -1, -1):
                ch = word[i]
                if ch not in curr.children:
                    ans.append(curr.val)
                    break
                else:
                    curr = curr.children[ch]
                    if i == 0:
                        ans.append(curr.val)
        return ans