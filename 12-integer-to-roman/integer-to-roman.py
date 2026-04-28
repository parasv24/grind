class Solution:
    def intToRoman(self, num: int) -> str:
        mp = {
            0: "",
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        def rec(num, cnt):
            if num == 0:
                return ""
            rem = num % 10
            sub_ans = ""
            mul = pow(10, cnt)
            if 1 <= rem <= 3:
                sub_ans = (rem - 0) * mp[mul]
            elif rem == 4:
                sub_ans = mp[mul] + mp[5 * mul]
            elif 6 <= rem <= 8:
                sub_ans = mp[5*mul] + (rem - 5) * mp[mul]
            elif rem == 9:
                sub_ans = mp[mul] + mp[mul * 10]
            else:
                sub_ans = mp[rem * mul]
            return rec(num//10, cnt + 1) + sub_ans
        return rec(num, 0) 
        