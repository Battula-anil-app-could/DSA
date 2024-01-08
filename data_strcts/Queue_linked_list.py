class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
    
    def __str__(self) -> str:
        current = self.head
        res = ""
        while current is not None:
            res += str(current.data)
            if current.next is not None:
                res += "-->"
            current = current.next 
        return res 
    
    def isEmpty(self):
        if self.head == None:
            return True 
        return False
    
    def enqueue(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node 
            self.tail = node 
        else:
            self.tail.next = node 
            self.tail = node 

    def dequeue(self):
        if self.head is not None:
            n = self.head
            self.head = self.head.next
            return n

