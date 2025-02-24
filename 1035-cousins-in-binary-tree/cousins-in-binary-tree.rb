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
# @param {Integer} x
# @param {Integer} y
# @return {Boolean}
def is_cousins(root, x, y)
    queue = []
    queue << root
    flag = false
    while queue.size > 0 do
        len = queue.size
        mp = {x: false, y: false}
        len.times do
            el = queue.shift
            mp[el.val] = true if [x,y].include?(el.val)
            els = []
            if el.left
                queue << el.left 
                els << el.left.val
            end
            if el.right
                queue << el.right
                els << el.right.val
            end
            return false if els.include?(x) && els.include?(y)
        end
        return true if mp[x] and mp[y]
    end
    false
end