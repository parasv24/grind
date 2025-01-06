class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        if len(boxes) == 1:
            return [0] 
        prefix_sums = []
        suffix_sums = []
        n = len(boxes)
        boxes = list(map(int,list(boxes)))
        for i in range(0, n):
            if i == 0:
                prefix_sums.append(boxes[i])
                suffix_sums.append(boxes[n - 1 - i])
            else:
                prefix_sums.append(boxes[i] + prefix_sums[i-1])
                suffix_sums.append(boxes[n-1-i]+ suffix_sums[i-1])
        for i in range(1,n):
            prefix_sums[i] += prefix_sums[i-1]
            suffix_sums[i] += suffix_sums[i-1]
        suffix_sums = suffix_sums[::-1]
        ans = []
        for i in range(0,n):
            if 0 < i < n-1:
                ans.append(prefix_sums[i-1] + suffix_sums[i+1])
            elif i == 0:
                ans.append(suffix_sums[i+1])
            else:
                ans.append(prefix_sums[i-1])
        return ans
        