class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if not node.child[idx]:
                node.child[idx] = TrieNode()
            node = node.child[idx]
        node.is_end = True

    def rec(self, word, i, node, cnt):
        if cnt > 2 or not node:
            return False

        if i == len(word):
            return node.is_end
        
        idx = ord(word[i]) - ord("a")
        if node.child[idx] and self.rec(word, i+1, node.child[idx], cnt):
            return True
        
        if cnt < 2:
            for c in range(26):
                if c == idx:
                    continue
                
                if node.child[c] and self.rec(word, i+1, node.child[c],cnt + 1):
                    return True
        return False
        
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        for w in dictionary:
            self.insert(w)
        
        res = []
        for q in queries:
            if self.rec(q, 0, self.root, 0):
                res.append(q)
        return res
        
        