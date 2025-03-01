# @param {Integer[]} nums
# @return {Integer[]}
def apply_operations(nums)
    og_size = nums.size
    nums.each_with_index { |n, i| nums[i], nums[i + 1] = n * 2, 0 if n == nums[i + 1] }
    nums.select!(&:positive?)
    nums += [0] * (og_size - nums.size) if og_size > nums.size
    nums
end