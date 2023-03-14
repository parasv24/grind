# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        output = [[-1 for i in range(n)] for j in range(m)]
        i,j,cur_d = 0,0,0
        d = [0,1,0,-1,0]
        temp = head
        while temp:
            output[i][j] = temp.val
            ni = i + d[cur_d]
            nj = j + d[cur_d + 1]
            if (min(ni, nj) < 0 or ni >= m or nj >= n or output[ni][nj] != -1):
                cur_d = (cur_d + 1)%4
            i += d[cur_d]
            j += d[cur_d+1]
            temp = temp.next
        return output