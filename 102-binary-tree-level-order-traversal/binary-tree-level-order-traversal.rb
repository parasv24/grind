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
# @return {Integer[][]}
def level_order(root)
    return [] unless root
    queue = []
    level = []
    queue << root
    while queue.size > 0 do
        len = queue.size
        temp = []
        len.times do
            el = queue.shift
            temp << el.val
            queue << el.left if el.left
            queue << el.right if el.right
        end
        level << temp
    end
    level
end