# @param {String[]} words
# @return {Integer}
def longest_palindrome(words)
    mp = Hash.new(0)
    ans = 0
    words.each do |word|
        rev = word.reverse
        if mp[rev] > 0
            ans += 4
            mp[rev] -= 1
        else
            mp[word] += 1
        end
    end
    mp.each do |key, value|
        if value > 0 && key == key.reverse
            ans += 2
            break
        end
    end
    ans
end