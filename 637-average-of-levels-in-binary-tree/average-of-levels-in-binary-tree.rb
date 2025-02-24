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
# @return {Float[]}
def average_of_levels(root)
    return [] unless root
    queue = []
    level = []
    queue << root
    while queue.size > 0 do
        len = queue.size
        temp = 0
        len.times do
            el = queue.shift
            temp += el.val
            queue << el.left if el.left
            queue << el.right if el.right
        end
        level << temp.fdiv(len)
    end
    level
end