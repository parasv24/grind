# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def maximum_importance(n, roads)
    deg = [0] * n
    roads.each do |x, y|
        deg[x]+= 1
        deg[y] += 1
    end
    deg.sort!
    ans = 0
    deg.reverse.each {|x| ans += (x * n); n-=1}
    ans
end