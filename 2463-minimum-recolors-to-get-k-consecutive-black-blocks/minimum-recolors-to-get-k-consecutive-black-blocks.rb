# @param {String} blocks
# @param {Integer} k
# @return {Integer}
def minimum_recolors(blocks, k)
    i , j, count,ans = 0, 0, 0, 101
    while j < blocks.size do
        size = j - i + 1
        count += 1 if blocks[j] == "W"
        if size == k
            ans = [ans, count].min
            count -= 1 if blocks[i] == "W"
            i+=1
        end
        j += 1
    end
    ans
end