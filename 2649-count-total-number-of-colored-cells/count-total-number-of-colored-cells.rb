# @param {Integer} n
# @return {Integer}
def colored_cells(n)
    1 + ((n-1) * (8 + (n-2)*4))/ 2
end