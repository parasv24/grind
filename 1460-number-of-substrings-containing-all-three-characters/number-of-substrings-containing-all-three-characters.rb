# @param {String} s
# @return {Integer}
def number_of_substrings(s)
    i ,j ,ans, temp = 0 , 0 , 0, ""
    counts = Hash.new(0)
    while j < s.size
        temp += s[j]
        counts[s[j]] += 1
        if counts["a"] > 0 && counts["b"] > 0 && counts["c"] > 0
            ans += s.size - j
            while counts["a"] > 0 && counts["b"] > 0 && counts["c"] > 0
                counts[s[i]] -= 1
                if counts["a"] > 0 && counts["b"] > 0 && counts["c"] > 0
                    ans += s.size - j
                end
                i += 1
            end
        end
        j += 1
    end
    ans
end