# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
    i , ans = 0 , 0
    while i < nums.size do
        if nums[i] == 0 
            if i + 2 >= nums.size
                return -1
            end
            nums[i] = 1
            nums[i+1] = 1 - nums[i+1]  # Toggle
            nums[i+2] = 1 - nums[i+2]  # Toggle
            ans += 1
        end
        i += 1
    end
    ans
end