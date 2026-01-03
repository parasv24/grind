class Solution:
    def numOfWays(self, n: int) -> int:
        A, B = 6, 6
        for i in range(2, n+1):
            newA = 2 * A + 2 * B
            newB = 2 * A + 3 * B
            A, B = newA, newB
        return (A+B)%1000000007

        


        




        