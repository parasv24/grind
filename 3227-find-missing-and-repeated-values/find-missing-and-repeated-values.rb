# @param {Integer[][]} grid
# @return {Integer[]}
def find_missing_and_repeated_values(grid)
    n = grid.size * grid.size
    sm = (n * (n+1)) / 2
    mp = Hash.new(0)
    a, b = -1, -1
    actual_sum = 0
    grid.each{|row| row.each{|el| mp[el]+= 1; actual_sum += el; a = el if mp[el] == 2}}
    [a, a + sm - actual_sum]
end
