# @param {Integer[][]} edges
# @return {Integer[]}
def find_redundant_connection(edges)
    @adj_list = Hash.new { |h, k| h[k] = [] }

    edges.each do |u, v|
        @adj_list[u] << v
        @adj_list[v] << u
    end

    @vis = Hash.new(false)
    @path = []
    def dfs(src, parent)
        @vis[src] = true
        @path << src
        @adj_list[src].each do |node|
            if @vis[node] && node != parent
                @path << node
                return true
            elsif @vis[node] == false
                return true if dfs(node, src) == true
            end
        end
        @path.pop
        false
    end
    dfs(1, -1)
    source = @path[-1]
    flag = false
    cycle_map = {}
    print(@path, "\n")
    @path.pop
    @path.each_with_index do |el, idx|
        flag = true if el == source
        cycle_map[el] = @path[idx+1] if flag == true
    end
    cycle_map[@path[-1]] = source
    print("cycle", flag, cycle_map, "\n")
    edges.reverse.each do |x, y|
        return [x, y] if cycle_map[x] == y || cycle_map[y] == x
    end
end