# @param {String} pattern
# @return {String}
def smallest_number(pattern)
  def helper(pattern, i, mp, ans)
    return ans if i == pattern.size

    val = ans[-1].to_i
    if pattern[i] == "I"
      left, right = val + 1, 9
    else
      left, right = 1, val - 1
    end

    (left..right).each do |idx|
      unless mp[idx]
        mp[idx] = true
        temp = helper(pattern, i + 1, mp, ans + idx.to_s)
        return temp if temp
        mp[idx] = false
      end
    end
    false
  end

  mp = {}
  (1..9).each do |val|
    mp[val] = true
    ans = helper(pattern, 0, mp, val.to_s)
    return ans if ans
    mp[val] = false
  end

  ""
end
