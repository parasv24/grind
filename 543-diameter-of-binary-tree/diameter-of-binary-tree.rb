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
def diameter_of_binary_tree(root)
    @maxi = -1
    def depth(node)
        return 0 unless node
        ld = depth(node.left)
        rd = depth(node.right)
        @maxi = [@maxi, ld + rd + 1].max
        return [ld,rd].max + 1
    end
    depth(root)
    return @maxi - 1
end