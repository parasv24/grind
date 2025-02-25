# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}
def max_path_sum(root)
    @maxi = -100000
    def helper(root)
        return 0 unless root
        ld = helper(root.left)
        ld = 0 if ld < 0
        rd = helper(root.right)
        rd = 0 if rd < 0
        @maxi = [@maxi, ld + rd + root.val].max
        return [ld + root.val, rd + root.val].max
    end
    helper(root)
    @maxi
end