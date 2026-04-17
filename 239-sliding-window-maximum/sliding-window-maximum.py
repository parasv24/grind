class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxD = deque()
        r = 0
        ans = []
        while r < len(nums):
            while maxD and nums[maxD[-1]] <= nums[r]:
                maxD.pop()
            maxD.append(r)
            if r - l == k - 1:
                ans.append(nums[maxD[0]])
                if maxD[0] == l:
                    maxD.popleft()
                l += 1
            # print(r, maxD, ans)
            r += 1
        return ans



        