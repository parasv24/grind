class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        mp = Counter(wordList)
        queue = [[beginWord,1]]
        mp[beginWord] = 2
        
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            
            for idx in range(len(word)):
                for ch in ascii_lowercase:
                    if idx == 0:
                        string = ch + word[1:]
                    elif idx == len(word) - 1:
                        string = word[:len(word)-1]+ ch
                    else:
                        string = word[:idx] + ch + word[idx+1:]
                    if mp[string] == 1:
                        mp[string] = 2
                        queue.append([string, length+1])
        return 0
        