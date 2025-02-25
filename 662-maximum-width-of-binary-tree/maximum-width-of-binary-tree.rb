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
def width_of_binary_tree(root)
    return 0 unless root
    queue = [[root, 0]]
    ans = -1
    while queue.size > 0
        len = queue.size
        first , last = 0, 0
        (0...len).each do |idx|
            el, index = queue.shift
            first = index if idx == 0
            last = index if idx == len - 1
            if el.left
                queue << [el.left, index * 2 + 1]
            end
            if el.right
                queue << [el.right, index * 2 + 2]
            end
        end
        ans = [ans, last - first + 1].max
    end
    ans
end