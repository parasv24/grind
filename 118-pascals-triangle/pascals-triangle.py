class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def rec(n):
            if n == 1:
                return [[1]]
            if n == 2:
                return [[1], [1,1]]
            small_ans = rec(n-1)
            last_arr = small_ans[-1]
            intut = [1]
            for i in range(1, len(last_arr)):
                intut.append(last_arr[i] + last_arr[ i - 1])
            intut.append(1)
            return small_ans + [intut]
        return rec(numRows)

            
        


        