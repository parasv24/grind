# @param {Integer[]} nums
# @return {Integer}
def longest_nice_subarray(nums)
    i,j,maxi, len, cur_xor, cur_sum = 0, 0, 0, 0, 0, 0
    while j < nums.size do
        len = j - i + 1
        cur_xor = cur_xor ^ nums[j]
        cur_sum += nums[j]
        maxi = [maxi, len].max if cur_xor == cur_sum 
        while cur_xor !=  cur_sum do
            cur_xor ^= nums[i]
            cur_sum -= nums[i]
            i += 1
        end
        j += 1
    end
    maxi
end