# @param {Integer[]} colors
# @param {Integer} k
# @return {Integer}
def number_of_alternating_groups(colors, k)
    colors += colors[0...k-1]
    counts, j, ans = [1] * colors.size, 1, 0
    print(counts, " ", j, ans, "\n")
    while j < colors.size do
        counts[j] = counts[j-1] + 1 if colors[j] != colors[j-1]
        ans += 1 if counts[j] >= k
        j += 1
    end
    ans
end