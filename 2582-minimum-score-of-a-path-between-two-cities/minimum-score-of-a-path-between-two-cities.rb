# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def min_score(n, roads)
  graph = Hash.new { |h, k| h[k] = [] }
  roads.each do |x,y,z|
    graph[x] << [y, z]
    graph[y] << [x, z]
  end
  queue = [1]
  vis = [false] * (n+1)
  mini = 10000000000
  while queue.size > 0
    node = queue.shift
    graph[node].each do |x,y|
      if vis[x] == false
        vis[x] = true 
        queue << x
      end
      mini = [mini, y].min
    end
  end
  mini
end