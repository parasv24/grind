# @param {Integer[]} arr
# @return {Integer}
def find_lucky(arr)
    mp = Hash.new(0)
    arr.each do |el|
        mp[el] += 1
    end
    ans = -1
    mp.each do |k,v|
        ans = [ans, k].max if k == v
    end
    ans
end