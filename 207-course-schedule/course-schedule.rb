# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish(num_courses, prerequisites)
  graph = Hash.new { |h, k| h[k] = [] }
  indegrees = [0] * num_courses
  prerequisites.each do |x, y|
    graph[x] << y
    indegrees[y] += 1
  end
  queue = []
  order = []
  print(indegrees, "\n")
  indegrees.each_with_index { |el, index| queue << index if el == 0 }
  print(queue, "\n")
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
  order.size == num_courses
end
