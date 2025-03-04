# @param {Integer} n
# @return {Boolean}
def check_powers_of_three(n)
    num = 1
    arr = []
    while num <= 10000000 do
        arr << num
        num *= 3
    end
    def is_possible(i, sum, arr)
        return true if sum == 0
        return false if i >= arr.size || sum < 0
        return is_possible(i+1, sum - arr[i], arr) || is_possible(i+1, sum, arr)
    end
    is_possible(0, n, arr)
end