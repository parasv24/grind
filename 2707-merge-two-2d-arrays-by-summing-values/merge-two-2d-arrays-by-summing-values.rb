# @param {Integer[][]} nums1
# @param {Integer[][]} nums2
# @return {Integer[][]}
def merge_arrays(nums1, nums2)
    i, j = 0, 0
    ans = []
    while i < nums1.size && j < nums2.size do
        if nums1[i][0] == nums2[j][0]
            ans << [nums1[i][0], nums1[i][1] + nums2[j][1]]
            i += 1
            j += 1
        elsif nums1[i][0] < nums2[j][0]
            ans << [nums1[i][0], nums1[i][1]]
            i += 1
        else
            ans << [nums2[j][0], nums2[j][1]]
            j += 1 
        end
    end
    ans.concat(nums1[i..-1]) if i < nums1.size
    ans.concat(nums2[j..-1]) if j < nums2.size
    ans
end