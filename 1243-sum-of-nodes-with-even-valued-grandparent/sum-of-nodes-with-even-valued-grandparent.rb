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
def sum_even_grandparent(root)
    def dfs(node, parent, grandpa)
        return 0 unless node
        ans = 0
        ans = node.val if grandpa && grandpa % 2 == 0
        return dfs(node.left, node.val, parent) + dfs(node.right, node.val, parent) + ans
    end
    dfs(root, nil, nil)
end