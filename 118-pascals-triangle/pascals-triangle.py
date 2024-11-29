class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1], [1,1]]
        numRows -= 2
        prev = [1,1]
        while numRows > 0:
            temp = [1]
            sm = prev[0]
            for i in range(1,len(prev)):
                sm += prev[i]
                temp.append(sm)
                sm -= prev[i-1]
            temp.append(1)
            ans.append(temp)
            prev = temp
            numRows -= 1
        return ans


        