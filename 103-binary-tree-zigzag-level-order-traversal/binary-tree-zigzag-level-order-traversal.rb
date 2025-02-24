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
def zigzag_level_order(root)
    return [] unless root
    queue = []
    level = []
    queue << root
    flag = 0
    while queue.size > 0 do
        len = queue.size
        temp = []
        len.times do
            el = queue.shift
            temp << el.val
            queue << el.left if el.left
            queue << el.right if el.right
        end
        temp.reverse! if flag == 1
        level << temp
        flag ^= 1
    end
    level
end