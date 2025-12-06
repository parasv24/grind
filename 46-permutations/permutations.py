class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(arr):
            ans=[]
            if len(arr)==1:
                return [arr]
            for i in range(0,len(arr)):
                newarr=arr[:i] + arr[i+1:]
                smallans=recur(newarr)
                for j in smallans:
                    ans.append([arr[i]]+j)
            return ans
        return recur(nums)
        