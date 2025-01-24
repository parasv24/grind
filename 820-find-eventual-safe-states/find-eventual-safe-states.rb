# @param {Integer[][]} graph
# @return {Integer[]}
def eventual_safe_nodes(graph)
  n = graph.size
  vis = Array.new(n, 0)
  path_vis = Array.new(n, 0)
  safe = Array.new(n, 0)
  define_method(:dfs) do |s, vis, path_vis, safe, graph|
    vis[s] = 1
    path_vis[s] = 1
    for el in graph[s]
      if vis[el] == 0
        if dfs(el, vis, path_vis, safe, graph)
          return true
        end
      elsif path_vis[el] == 1
        return true
      end
    end
    path_vis[s] = 0
    safe[s] = 1
    false
  end
  (0...n).each do |i|
    dfs(i, vis, path_vis, safe, graph) if vis[i] == 0
  end

  safe.each_index.select { |i| safe[i] == 1 }
end
