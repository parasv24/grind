class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def get_all_indices(s, word):
            combined = word + "#" + s
            lps = [0] * len(word)
            i = 1
            length = 0
            indices = []
            while i < len(combined):
                if combined[i] == combined[length]:
                    length += 1
                    if i < len(word):
                        lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        i += 1
                if length == len(word):
                    indices.append(i - length - length - 1)
            return indices
        
        mp = {}
        buckets = defaultdict(list)
        st = set()
        for word in words:
            if word not in st:
                st.add(word)
                indexes = get_all_indices(s, word)
                for idx in indexes:
                    mp[idx] = word
                    buckets[(idx % len(word))].append(idx)
        word_len = len(words[0])
        cnt = Counter(words)
        ans = []
        for _, values in buckets.items():
            values.sort()
            inmp = defaultdict(int)
            word_count = 0
            j = 0
            i = 0
            while j < len(values):
                idx = values[j]
                word = mp[idx]
                inmp[word] += 1
                word_count += inmp[word] == cnt[word]
                idx = -1
                while i <= j and word_count == len(cnt.keys()):
                    if word_count == len(cnt.keys()):
                        idx = values[i]
                    if inmp[mp[idx]] == cnt[mp[idx]]:
                        word_count -= 1
                    inmp[mp[idx]] -= 1
                    i += 1
                if idx != -1 and (values[j] - idx + len(word)) == len(words) * len(word):
                    ans.append(idx)
                j += 1
        return ans
            