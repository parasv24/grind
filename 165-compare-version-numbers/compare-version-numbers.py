class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_arr = version1.split(".")
        v2_arr = version2.split(".")
        diff = abs(len(v2_arr) - len(v1_arr))
        if len(v1_arr) < len(v2_arr):
            v1_arr.extend(["0"] * diff)
        else:
            v2_arr.extend(["0"]* diff)
        for i in range(len(v1_arr)):
            num1, num2 = int(v1_arr[i]), int(v2_arr[i])
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        return 0
        