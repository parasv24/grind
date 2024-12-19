class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mp = {}
        og_map = {}
        for el in word:
            og_map[el] = og_map.get(el, 0) + 1
        ans = [0] * 26
        # print(arr)
        for el in word:
            # print(el, mp, ans, sep="\n")
            mp[el] = mp.get(el , 0) + 1
            if ord(el) < 97:
                num = ord(el)
                if og_map.get(chr(num),0) > 0 and og_map.get(chr(num + 32),0):
                    if mp.get(chr(num+32),-4) == og_map.get(chr(num+32),-5) and ans[num-65] >=0:
                        ans[num-65] = 1
                    else:
                        ans[num-65] = -1
        # print(ans, mp, og_map)
        final_ans = 0
        for el in ans:
            if el == 1:
                final_ans += el
        return final_ans