# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = (len(nums)-1)//2
        new_node = TreeNode(nums[mid])
        new_node.left = self.sortedArrayToBST(nums[0:mid])
        new_node.right = self.sortedArrayToBST(nums[mid+1:])
        return new_node
        