# @param {Integer[]} nums
# @return {Integer}
def find_lhs(nums)
    ans = 0
    counter = Hash.new(0)
    nums.each do |item|
        counter[item] += 1
    end

    sorted_counter = counter.sort_by {|k, v| k}
    
    sorted_counter.each_cons(2) do |(k1, v1), (k2, v2)|
        if k2 - k1 == 1
            ans = [ans, v1 + v2].max
        end
    end
    ans
end