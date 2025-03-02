# @param {Integer} n
# @param {Integer[][]} dislikes
# @return {Boolean}
def possible_bipartition(n, dislikes)
    @adj_list = Hash.new { |h, k| h[k] = [] }

    dislikes.each do |u, v|
        @adj_list[u] << v
        @adj_list[v] << u
    end

    @vis = [-1] * (n+1)
    def bfs(src)
        queue = [[src, 0]]
        @vis[src] = 0
        while !queue.empty? do
            el, color = queue.shift
            new_color = color ^ 1
            @adj_list[el].each do |node|
                if @vis[node] == -1
                    @vis[node] = new_color
                    queue << [node, new_color]
                elsif @vis[node] != new_color
                    return false
                end
            end
        end
    end
    @adj_list.each do |k,_|
        if @vis[k] == -1
            #print(@vis, k)
            return false if bfs(k) == false
        end
    end
    #print(@vis)
    true
end