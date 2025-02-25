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
# @param {Integer} target_sum
# @return {Boolean}
def has_path_sum(root, target_sum)
    return false if root.nil?
    def helper(root, target_sum)
        return false if root.nil?
        return true if root.left.nil? && root.right.nil? && target_sum == root.val
        return helper(root.left, target_sum - root.val) || helper(root.right, target_sum - root.val)    
    end
    helper(root, target_sum)
end