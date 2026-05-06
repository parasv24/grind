class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def rec(i):
            next_i = -1
            length = 0
            words_arr = []
            for j in range(i, len(words)):
                if len(words_arr) > 0:
                    if length + 1 + len(words[j]) > maxWidth:
                        next_i = j
                        break
                    length += 1
                length += len(words[j])
                words_arr.append(words[j])
            if next_i == -1:
                return [" ".join(words_arr) + " " * (maxWidth - length)]
            if len(words_arr) == 1:
                small_ans = words_arr[0] + " " * (maxWidth - len(words_arr[0]))
            else:
                extra_spaces = (maxWidth - length) // (len(words_arr) - 1)
                extra_ones = (maxWidth - length) % (len(words_arr) - 1)
                print(i, extra_spaces, extra_ones, length)
                small_ans = ""
                for word in words_arr:
                    if len(small_ans) > 0:
                        small_ans += (" " +  (" " * extra_spaces) + (" " * int(extra_ones > 0) ))
                        extra_ones -= 1
                    small_ans += word
            next_ans = []
            print(i, next_i)
            if next_i > -1:
                next_ans =  rec(next_i)
            return [small_ans] + next_ans
        return rec(0)