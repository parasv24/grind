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
# @return {Integer[]}
def right_side_view(root)
    return [] unless root
    queue = []
    level = []
    queue << root
    while queue.size > 0 do
        len = queue.size
        prev = nil
        len.times do
            el = queue.shift
            prev = el.val
            queue << el.left if el.left
            queue << el.right if el.right
        end
        level << prev
    end
    level
end