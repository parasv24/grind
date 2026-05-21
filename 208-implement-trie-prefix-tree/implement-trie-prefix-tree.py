class Node:
    def __init__(self):
            self.children = [0] * 26
            self.is_end = False
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if curr.children[idx] == 0:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.is_end = True

        

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if curr.children[idx] == 0:
                return False
            curr = curr.children[idx]
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if curr.children[idx] == 0:
                return False
            curr = curr.children[idx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)