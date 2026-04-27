class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def get_all_indices(string, pat):
            combined = pat + "#" + string
            lps = [0] * len(pat)
            i = 1
            length = 0
            indices = []
            while i < len(combined):
                if combined[i] == combined[length]:
                    length += 1
                    if i < len(pat):
                        lps[i] = length
                    i += 1
                else:
                    if length > 0:
                        length = lps[length-1]
                    else:
                        i += 1
                if length == len(pat):
                    indices.append(i - length - length - 1)
            return indices
        indices_a = get_all_indices(s, a)
        indices_b = get_all_indices(s, b)
        ans = []
        if len(indices_b) == 0 or len(indices_a) == 0:
            return []
        max_l = indices_b[-1] + k + 2
        line = [0] * max_l
        for idx in indices_b:
            start_idx = max(0, idx - k)
            end_idx = min(idx + k, max_l - 2)
            line[start_idx] += 1
            line[end_idx+1] -= 1
        prev = 0
        for idx in range(max_l):
            line[idx] += prev
            prev = line[idx]
        
        # print(line, len(line))
        for idx in indices_a:
            if idx < max_l and line[idx]!=0:
                ans.append(idx)

        return ans
        