class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None


class DBCLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.length = 0 

    def __str__(self):
        res = ""
        node = self.head 
        while node is not None:
            res += str(node.value)
            if node.next == self.head:
                return res
            res += "<-->"
            node = node.next
        return res
    

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node 
            self.head.prev = node
            self.tail = node 
            self.tail.next = node 
        else:
            self.tail.next = node
            node.prev = self.tail 
            self.tail = node
            node.next = self.head
            self.head.prev = self.tail 
        self.length += 1 
        
    def prepend(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node 
            self.tail = node 
            self.tail.next = self.head 
            self.head.prev = self.tail 
        else:
            self.tail.next = node
            node.next  =self.head 
            self.head.prev = node
            self.head = node 
            self.head.prev = self.tail 
        self.length += 1
    
    def pop(self, index = False):
        if index == False:
            if self.head == None:
                raise ValueError("Index Out Of Range")
            else:
                if self.length == 1:
                    self.head = None 
                    self.tail = None 
                    self.length = 0 
                else:
                    prev = self.tail.prev 
                    self.tail.prev = None
                    self.tail.next = None
                    self.tail =   prev
                    self.tail.next = self.head 
                    self.head.prev = self.tail
                    self.length -= 1 
        else:
            if index < 0:
                index = self.length + index 
            if index < 0 or index >= self.length:
                raise ValueError("Index Out Of Range")
            else:
                if self.length == 1:
                    if index == 0:
                        self.head == None 
                        self.tail = None 
                        self.length = 0 
                    else:
                        raise ValueError("Index Out Of Range")
                else:
                    if index == self.length -1:
                        self.pop()
                    else:
                        poped_node = self.head 
                        
                        for i in range(index):
                            poped_node = poped_node.next 
                        
                        poped_node.prev.next= poped_node.next
                        poped_node.prev = None 
                        poped_node.next = None 
                        self.length -= 1 
                        
    def insert(self, index, value):
            node = Node(value)
            if index < 0 :
                index = self.length + index 
            if self.head is not None:
                if index < 0 or index >=self.length:
                    raise ValueError("Index Out Of Range")
                else:
                    if index == 0:
                        self.prepend(value) 
                    elif index == self.length-1:
                        self.append(value)
                    else:
                        target_node = self.head 
                        for i in range(index):
                            target_node = target_node.next 
                        node.next = target_node 
                        node.prev = target_node.prev 
                        target_node.prev.next = node 
                        target_node.prev = node 
                        self.length += 1  
            else:
                if index == 0:
                    self.append(value)
                else:
                    raise ValueError("Index Out Of Range")
    
    def index(self, value):
        count = 0 
        node = self.head 
        while node is not None:
            if node.value == value:
                return count 
            if node.next == self.head:
                raise ValueError("Value Not Found")
            else:
                node = node.next 
                count += 1 
    
    def get(self, index):
        node = self.head 
        if index < 0:
            index = self.length + index 
        if index < 0 or index >=self.length:
            raise ValueError("Index Out Of Range")
        else:
            for _ in range(index):
                node = node.next 
            return node.value
            
    def remove(self, value):
        index = self.index(value)
        self.pop(index)
                    
    def delete(self):
        self.head = None 
        self.tail = None 
        self.length = 0 
    
    def set(self, index, value):
        if index < 0:
            index = self.length + index 
        if index < 0 or index >= self.length:
            raise ValueError("Index Out Of Range")
        else:
            node = self.head 
            for _ in range(index):
                node = node.next 
            node.value = value 
            
            

my_linked_list = DBCLinkedList()
my_linked_list.insert(0, 2)
my_linked_list.pop()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.prepend(4)
my_linked_list.prepend(5)
my_linked_list.pop()
print(my_linked_list)
my_linked_list.pop(-1)
my_linked_list.insert(1, 6)
my_linked_list.insert(2, 7)
my_linked_list.insert(0, 8)
my_linked_list.insert(-1, 9)
print(my_linked_list.index(1))
print(my_linked_list.get(1))
my_linked_list.set(-1, 10)
print(my_linked_list)