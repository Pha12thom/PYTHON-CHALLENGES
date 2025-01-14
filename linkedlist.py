class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        
        while True:
            if currentNode.next is None:
                currentNode.next = node
                break
            currentNode = currentNode.next
            
LL = LinkedList()
LL.insert(1)
LL.insert(2)
print(LL.head) # Output: 1