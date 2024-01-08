class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None


class CSLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0 
    
    def __str__(self):
        current = self.head 
        result = ""
        while current is not None:
            result += str(current.value)
            current = current.next 
            if current == self.head:
                break 
            result += "-->"
        return result 

    def append(self, value):
        node = Node(value)
        if self.head is None:
            node.next = node 
            self.head = node 
            self.tail = node
            self.length += 1 
            
        else:
            self.tail.next = node 
            node.next = self.head 
            self.tail = node 
            self.length += 1

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node 
            self.tail = node 
            node.next = node
            self.length += 1 
        else:
            temp = self.head
            self.head = node 
            self.head.next = temp 
            self.tail.next = node
            self.length += 1 

    def pop(self, index = False):
        if index is not False:
            if self.head is None:
                if self.length == 0:
                    raise ValueError("Index Out Of Range")
            else:
                poped_node = self.head 
                if index < 0:
                    index = self.length + index 
                if index  < 0 or index >= self.length:
                    raise ValueError("Index Out Of Range")
                for _ in range(index):
                    poped_node = poped_node.next 
                if poped_node == self.head:
                    self.head = poped_node.next 
                    self.tail.next = self.head
                    poped_node.next = None 
                elif poped_node == self.tail:
                    pre_node = self.head 
                    for _ in range(index-1):
                        pre_node = pre_node.next  
                    self.tail = pre_node 
                    self.tail.next = self.head 

                else:
                    pre_node = self.head 
                    for _ in range(index-1):
                        pre_node = pre_node.next 
                    pre_node.next = pre_node.next.next 
                self.length -= 1
        else:
            if self.length == 0:
                raise ValueError("Index Out Of Range")
            elif self.length == 1:
                self.head = None 
                self.tail = None 
                self.length = 0 
            else:
                pointer = 0 
                current = self.head 
                while current is not None:
                    pointer += 1 
                    current = current.next 
                    if current == self.head:
                        break 
                pointer -= 1 

                pre_node = self.head
                for _ in range(pointer -1):
                    pre_node = pre_node.next 
                self.tail = pre_node 
                self.tail.next = self.head 
                self.length -= 1 

    def insert(self, index, value):
        node = Node(value)
        if self.length == 0:
            raise ValueError("Index Out Of Range")
        else:
            if index < 0:
                index = self.length + index 
            if index < 0 or index >=self.length:
                raise ValueError("Index Out Of Index")
            if self.length == 1:
                if index == 0:
                    self.head = node 
                    self.tail = node 
                    node.next = node 
                else:
                    raise ValueError("Index Out Of Range")
            else:
                if index == 0:
                    temp = self.head
                    self.head = node 
                    self.head.next = temp 
                    self.tail.next = self.head 
                else:
                    target_node = self.head 
                    pre_node = self.head 
                    for _ in range(index):
                        target_node = target_node.next 
                    for _ in range(index-1):
                        pre_node = pre_node.next 
                    pre_node.next = node 
                    node.next = target_node 
            self.length += 1 
    
    def index(self, value):
        count = 0 
        current = self.head 
        while True:
            if current.value == value:
                return count 
            count += 1 
            current = current.next 
            if current == self.head:
                break 
        return None 
    
    def get(self, index):
        if index < 0:
            index = self.length + index 
        if index < 0 or index >= self.length:
            raise ValueError("Index Out Of Range")
        else:
            current = self.head 
            for _ in range(index):
                current = current.next 
            return current.value 
    
    def remove(self, value):
        if self.index(value):
            self.pop(self.index(value))
            return True
        else:
            return False
        
    def delete(self):
        self.head = None 
        self.tail = None 
        self.length = 0 
    



        
                
                
                
            

my_linked_list = CSLinkedList()

my_linked_list.append(1)
my_linked_list.prepend(3)
my_linked_list.prepend(4)
my_linked_list.insert(0, 2)
print(my_linked_list.index(4))
print(my_linked_list.remove(1))
print(my_linked_list)

