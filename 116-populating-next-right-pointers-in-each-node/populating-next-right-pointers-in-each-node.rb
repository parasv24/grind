# Definition for Node.
# class Node
#     attr_accessor :val, :left, :right, :next
#     def initialize(val)
#         @val = val
#         @left, @right, @next = nil, nil, nil
#     end
# end

# @param {Node} root
# @return {Node}
def connect(root)
    return root unless root
    queue = []
    queue << root
    while queue.size > 0 do
        len = queue.size
        prev = nil
        len.times do
            el = queue.shift
            prev.next = el if prev
            prev = el
            queue << el.left if el.left
            queue << el.right if el.right
        end
    end
    root
end