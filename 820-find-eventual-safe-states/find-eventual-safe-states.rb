# @param {Integer[][]} graph
# @return {Integer[]}
def eventual_safe_nodes(graph)
    n = graph.size
    vis = Array.new(n, 0)
    path_vis = Array.new(n, 0)
    safe = Array.new(n, 0)
    def dfs(s, vis, path_vis, graph, safe)
        vis[s] = 1
        path_vis[s] = 1
        (graph[s]).each do |el|
        if vis[el] == 0
            if dfs(el, vis, path_vis, graph, safe)
            return true
            end
        elsif path_vis[el] == 1
            return true
        end
        end
        path_vis[s] = 0
        safe[s] = 1
        return false
    end
  (0...n).each do |i|
    dfs(i, vis, path_vis, graph, safe) if vis[i] == 0
  end
   return (0...n).select do |i|
    safe[i] == 1
  end
end