# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Integer[]}
def find_order(num_courses, prerequisites)
  graph = Hash.new { |h, k| h[k] = [] }
  indegrees = [0] * num_courses
  prerequisites.each do |x, y|
    graph[y] << x
    indegrees[x] += 1
  end
  queue = []
  order = []
  indegrees.each_with_index { |el, index| queue << index if el == 0 }
  while !queue.empty?
    el = queue.shift
    order  << el
    graph[el].each do |node|
      if indegrees[node] != 0
        indegrees[node] -= 1
        queue << node if indegrees[node] == 0
      end
    end
  end
  order.size == num_courses ? order : []
end