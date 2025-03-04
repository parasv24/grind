# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[]}
def find_smallest_set_of_vertices(n, edges)
    ins = [0] * n
    edges.each do |x, y|
        ins[y] += 1
    end
    ans = []
    ins.each_with_index do |el, idx|
        ans << idx if el == 0
    end
    ans
end