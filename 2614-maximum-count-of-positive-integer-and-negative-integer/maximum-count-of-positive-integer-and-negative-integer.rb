# @param {Integer[]} nums
# @return {Integer}
def maximum_count(nums)
    [nums.count(&:negative?),nums.count(&:positive?)].max
end