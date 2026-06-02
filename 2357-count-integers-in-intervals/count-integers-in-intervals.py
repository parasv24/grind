class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0
        self.lazy = False

class CountIntervals:

    def __init__(self):
        self.root = Node()
        

    def add(self, left: int, right: int) -> None:
        def update(node, l, r, left, right):
            if node.val == r - l + 1:
                return
            
            if r < left or l > right:
                return
                                        
            if left <= l and r <= right:
                node.val = r - l + 1
                node.lazy = True
                return
            
            if node.lazy:
                node.val = r - l + 1
                if not node.left:
                    node.left = Node()
                node.left.lazy = True
                if not node.right:
                    node.right = Node()
                node.right.lazy = True
                node.lazy = False
            
            mid = (l+r) // 2
            if not node.left:
                node.left = Node()
            if not node.right:
                node.right = Node()
            
            update(node.left, l, mid, left, right)
            update(node.right, mid + 1, r, left, right)
            node.val = node.left.val + node.right.val
            return
        
        update(self.root, 1, 10 ** 9, left, right)
        return

            

        

    def count(self) -> int:
        return self.root.val
        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()