# @param {Integer} left
# @param {Integer} right
# @return {Integer[]}
def closest_primes(left, right)
    def is_prime(num)
        sqrt = (num ** 0.5).to_i
        (2..sqrt).each do |val|
            return false if num % val == 0
        end
        true
    end
    flag = false
    x, y = -1,-1
    ans = 1000000000
    prev = -1000000000
    final_ans = [-1, -1]
    left += 1 if left == 1
    (left..right).each do |val|
        if is_prime(val)
            y = val
            final_ans, ans = [prev, y], y - prev if y - prev < ans
            return final_ans if ans <= 2
            prev = y
        end
    end
    final_ans
end