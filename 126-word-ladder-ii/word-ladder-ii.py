class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        mp = Counter(wordList)
        queue = [[beginWord,1]]
        mp[beginWord] = 2
        path = [beginWord]
        dps = defaultdict(list)
        max_depth = -1
        while queue:
            word, length = queue.pop(0)
            dps[length].append(word)
            if word == endWord:
                max_depth = length
                break
            
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
        ans = []
        vis = {}
        def dfs(depth, word, path=[]):
            vis[word] = True
            if depth <= 1:
                if word == beginWord:
                    ans.append(path)
                return
            for word1 in dps[depth-1]:
                for idx in range(len(word)):
                    for ch in ascii_lowercase:
                        if idx == 0:
                            string = ch + word[1:]
                        elif idx == len(word) - 1:
                            string = word[:len(word)-1]+ ch
                        else:
                            string = word[:idx] + ch + word[idx+1:]
                        if string == word1:
                            dfs(depth - 1, word1, [word1] + path)
                            break
        dfs(max_depth,endWord, [endWord])
        return ans
            
            
        