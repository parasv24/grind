# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_pairs(n, edges)
    graph = Hash.new { |h, k| h[k] = [] }
    edges.each do |x, y|
        graph[x] << y
        graph[y] << x
    end
    vis = [false] * n
    def dfs(src, graph, vis)
        vis[src] = true
        ans = 1
        graph[src].each do |el|
            ans += dfs(el, graph, vis) unless vis[el]
        end
        return ans
    end
    comps = []
    (0...n).each do |node|
        comps << dfs(node, graph ,vis) unless vis[node]
    end
    return 0 if comps.size == 1
    ans = 0
    comps.each do |size|
        ans += size * (n - size)
    end

    ans / 2
end