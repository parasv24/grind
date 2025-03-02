# @param {Integer[][]} rooms
# @return {Boolean}
def can_visit_all_rooms(rooms)
    queue = [0]
    vis = [0] * rooms.size
    vis[0] = 1
    while !queue.empty? do
        el = queue.shift
        rooms[el].each{|room| queue << room if vis[room] == 0; vis[room] = 1}
    end
    vis.sum == rooms.size
end