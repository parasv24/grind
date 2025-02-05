# @param {String} s1
# @param {String} s2
# @return {Boolean}
def are_almost_equal(s1, s2)
  return false if s1.length != s2.length
  
  diff = []
  
  (0...s1.length).each do |i|
    diff << i if s1[i] != s2[i]
  end
  
  return true if diff.empty?
  
  return false unless diff.length == 2
  
  s1[diff[0]] == s2[diff[1]] && s1[diff[1]] == s2[diff[0]]
end