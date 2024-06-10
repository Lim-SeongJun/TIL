class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
class CircularLinkedList:
    def __init__(self):
        self.last = None
    def insert(self,data):
        n = Node(data,None)
        print(n.data)
        if self.last is None:
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

myCLL = CircularLinkedList()
myCLL.insert(1)
myCLL.insert(2)
myCLL.insert(3)