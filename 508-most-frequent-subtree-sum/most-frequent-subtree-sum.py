# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        mp = {}
        mx_value = -1
        def get_subtree_sums(root, mx_value):
            if not root.left and not root.right:
                cnt = mp.get(root.val, 0)
                mp[root.val] = cnt + 1
                if cnt + 1 > mx_value:
                    mx_value = cnt + 1 
                return root.val, mx_value
            left_sum = 0
            right_sum = 0
            if root.left:
                left_sum, mx_value= get_subtree_sums(root.left, mx_value)
            if root.right:
                right_sum, mx_value = get_subtree_sums(root.right, mx_value)
            sum_val = left_sum + right_sum + root.val
            cnt = mp.get(sum_val, 0)
            mp[sum_val] = cnt + 1
            if cnt + 1 > mx_value:
                mx_value = cnt + 1 
            return sum_val, mx_value
        subs, mx_value = get_subtree_sums(root, -1)
        arr = []
        for i in mp.keys():
            if mp[i] == mx_value:
                arr.append(i)
        return arr

                

        