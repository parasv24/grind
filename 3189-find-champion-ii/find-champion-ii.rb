# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def find_champion(n, edges)
  ins = [0] * n
  edges.each do |x,y|
    ins[y] += 1
  end  
  flag = false
  ans = -1
  ins.each_with_index do |val, idx|
    return -1 if val == 0 && flag
    ans, flag = idx, true if val == 0
  end
  ans
end