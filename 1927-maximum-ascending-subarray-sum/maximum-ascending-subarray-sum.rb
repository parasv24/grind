# @param {Integer[]} nums
# @return {Integer}
def max_ascending_sum(nums)
    maxi = nums[0]
    cur = nums[0]
    leng = nums.length
    (1...leng).each do |idx|
        if nums[idx] > nums[idx-1]
            cur += nums[idx]
        else
            cur = nums[idx]
        end
        maxi = [maxi, cur].max
    end
    maxi
end