# @param {Integer[]} nums
# @return {Integer[]}
def build_array(nums)
    nums.collect {|num| nums[num]}
end