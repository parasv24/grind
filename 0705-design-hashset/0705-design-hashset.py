class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
class MyHashSet:

    def __init__(self):
        self.head = Node(-1)

    def add(self, key: int) -> None:
        temp = self.head
        while(temp.next):
            if temp.val == key:
                return False
            temp = temp.next
        if temp.val != key:    
            temp.next = Node(key)
            return True
        else:
            return False

    def remove(self, key: int) -> None:
        temp = self.head
        pre = None
        while(temp.next):
            if temp.val == key:
                break
            pre = temp        
            temp = temp.next
        
        if pre and pre.next.val == key:
            pre.next = temp.next 

    def contains(self, key: int) -> bool:
        temp = self.head
        while(temp):
            if temp.val == key:
                return True
            temp = temp.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)