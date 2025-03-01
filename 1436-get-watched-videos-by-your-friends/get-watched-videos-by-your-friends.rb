# @param {String[][]} watched_videos
# @param {Integer[][]} friends
# @param {Integer} id
# @param {Integer} level
# @return {String[]}
def watched_videos_by_friends(watched_videos, friends, id, level)
    queue = [id]
    lvl = 0
    vis = [false] * friends.size
    vis[id] = true
    mp = Hash.new(0)
    while queue.size > 0 do 
        length = queue.size
        length.times do
            el = queue.shift
            if lvl == level
                watched_videos[el].each{|vid| mp[vid] += 1}
            end
            friends[el].each do |new_el|
                queue << new_el unless vis[new_el]
                vis[new_el] = true
            end
        end
        break if lvl == level
        lvl += 1
    end
    mp.sort_by { |k, v| [v, k] }.map { |k, _| k }
end