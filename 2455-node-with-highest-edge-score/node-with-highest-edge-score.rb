# @param {Integer[]} edges
# @return {Integer}
def edge_score(edges)
    ins = [0] * edges.size
    maxi, ans = -1, -1 
    edges.each_with_index do |x, index|
        ins[x] += index
        ans = [x, ans].min if ins[x] == maxi
        ans, maxi = x, ins[x] if ins[x] > maxi
    end
    ans
end