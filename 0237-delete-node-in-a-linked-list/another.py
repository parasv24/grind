class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val  #we can only delete node we stand befor it #to delete given node copy val 
                                  #of next node to our val and then delete next node
                                  #first become next node and now delete next node, we can now do this as we
                                  #stand before the nextnode
                                  #so effectively delete ourselves
                        
        node.next = node.next.next
