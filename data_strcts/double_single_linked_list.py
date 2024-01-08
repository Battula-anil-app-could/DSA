class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

   


class DSLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.length = 0
    
    def __str__(self):
        node = self.head 
        result = ""
        while node is not None:
            result += str(node.value)
            if node.next is not None:
                result += "<-->"
            node = node.next 
        return result
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node 
            self.tail = node 
        else:
            self.tail.next = node 
            self.tail = node 
            self.tail.prev = self.head 
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node 
            self.tail = node
        else: 
            node.next = self.head
            self.head.prev = node 
            self.head = node 
        self.length += 1 
    
    def insert(self, index, value):
        node = Node(value)

        if index < 0:
            index = self.length  + index 
        if index < 0 or index >= self.length:
            raise ValueError("Index Out Of Range")
        else:
            if index == 0:
                self.prepend(value)
            else:
                prev_node = self.head 
                for _ in range(index-1):
                    prev_node = prev_node.next 
                prev_node.next.prev = node 
                node.next = prev_node.next 
                prev_node.next  = node 
                node.prev = prev_node 
                self.length += 1 
    
    def pop(self, index = False):
        if index is False:
            prev_node = self.tail.prev 
            self.tail.prev  = None
            self.tail = prev_node 
            self.tail.next = None
            self.length -= 1 
        else:
            if index < 0:
                index = self.length + index 
            if index < 0 or index >= self.length:
                raise ValueError("Index Out Of Range")
            else:
                prev_node = self.head 
                for _ in range(index - 1):
                    prev_node = prev_node.next 
                if index == 0:
                    self.head.next.prev = None
                    self.head = self.head.next 
                elif prev_node.next == self.tail:
                    self.tail.prev = None
                    self.tail = prev_node
                    self.tail.next = None
                else:
                    prev_node.next.next.prev = prev_node 
                    prev_node.next = prev_node.next.next 
                self.length -= 1 
    
    def index(self, value):
        if self.head is None:
            raise ValueError("Value Not Found")
        else:
            node = self.head 
            count = 0 
            for _ in range(self.length):
                if node.value == value:
                    return count 
                count += 1  
                node = node.next
            raise ValueError("Value Not Found")
    
    def get(self, index):
        if self.head is None:
            raise ValueError("Value Not Found")
        else:
            node = self.head 
            for _ in range(index):
                node = node.next 
            return node.value 
            
    def remove(self, value):
        index = self.index(value)
        self.pop(index)

    def set(self, index, value):
        prev_value = self.get(index)

        cur = self.head 
        while cur is not None:
            if cur.value == prev_value:
                cur.value = value 
                break 
    def reverse(self):
        node = self.tail 
        while node is not None:
            print(node.value)
            node = node.prev 
        



my_linked_list = DSLinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.prepend(3)
my_linked_list.insert(-1, 6)
my_linked_list.pop(0)
print(my_linked_list.index(6))
print(my_linked_list.get(1))
print(my_linked_list)
my_linked_list.remove(6)
my_linked_list.set(0, 18)
print(my_linked_list)
my_linked_list.reverse()


