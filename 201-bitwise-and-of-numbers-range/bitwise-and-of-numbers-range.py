class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left = bin(left)[2:].zfill(32)
        right = [c for c in bin(right)[2:].zfill(32)]

        idxs = set()
        for i in range(32):
            if left[i] == right[i] and left[i] == '1':
                new_one = right[:]
                new_one[i] = "0"
                if "".join(new_one) >= left:
                    idxs.add(i)
        ans = [0] * 32
        for i in range(32):
            if left[i] == right[i] and left[i] == '1' and i not in idxs:
                ans[i] = 1
        # print(ans)
        answer = 0
        for i in range(32):
            answer = answer * 2 + ans[i]
        return answer
        
        