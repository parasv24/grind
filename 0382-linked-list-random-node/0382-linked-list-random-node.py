# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        count = 0
        result = None
        curr = self.head

        while curr:
            count += 1
            # generate a random number between 1 and the count
            # if the random number is 1, update the result with the current node's value
            if random.randint(1, count) == 1:
                result = curr.val
            curr = curr.next

        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()