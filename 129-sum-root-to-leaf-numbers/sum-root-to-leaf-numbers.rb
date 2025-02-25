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
def sum_numbers(root)
    return 0 if root.nil?
    @total = 0
    def helper(root, cur)
        if root.left.nil? and root.right.nil?
            @total += (cur * 10 + root.val)
            return
        end
        helper(root.left, cur * 10 + root.val) if root.left
        helper(root.right, cur * 10 + root.val) if root.right
    end
    helper(root, 0)
    @total
end