class Node:
    def __init__(self, key, val, next = None):
        self.val = val
        self.key = key
        self.next = next
class MyHashMap:

    def __init__(self):
        self.head = Node(-1, -1)
        

    def put(self, key: int, value: int) -> None:
        temp = self.head
        while(temp.next):
            if temp.key == key:
                temp.val = value
                return
            temp = temp.next
        if temp.key != key:    
            temp.next = Node(key, value)
            return
        else:
            temp.val = value

    def get(self, key: int) -> int:
        temp = self.head
        while(temp):
            if temp.key == key:
                return temp.val
            temp = temp.next
        return -1

    def remove(self, key: int) -> None:
        temp = self.head
        pre = None
        while(temp.next):
            if temp.key == key:
                break
            pre = temp        
            temp = temp.next
        
        if pre and pre.next.key == key:
            pre.next = temp.next 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)