class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 


class LinkedList:

    def __init__(self):
        self.head = None
        self.tile  = None 
        self.length = 0

    def __str__(self):
        tem_node = self.head 
        result = ''
        while tem_node is not None:
            result += str(tem_node.value)
            if tem_node.next is not None:
                result += "-->"
            tem_node = tem_node.next 
        if result == '':
            return "None"
        return result
    
    def append(self, value):
        new_node = Node(value)  
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1 

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head 
        if self.head is None:
            if index == 0:
                self.head = new_node 
                self.tail = new_node 
                self.length += 1
            else:
                raise ValueError("Index Out Of Range")
        else:
            if index == 0:
                self.prepend(value)
            else:
                if index < 0:
                    index = self.length + index +1
                if index > self.length or index < 0:
                    raise ValueError(f"Index Out Of Range" )
                else:
                    for _ in range(index-1):
                        temp_node = temp_node.next
                    
                    new_node.next = temp_node.next 
                    temp_node.next = new_node 

                    self.length += 1 

    def traves(self):
        current = self.head 
        ls = []
        while current is not None:
            ls.append(current.value)
            current = current.next 
        return ls
    def index(self, value):
        current = self.head 
        i = 0
        while current is not None:
            if current.value == value:
                return i
            current = current.next 
            i += 1 
        return None
    
    def get(self, index):
        if index < 0:
            index = self.length + index 
        if index < 0:
            raise ValueError("Index Out Of Range")
        temp_node = self.head
        for _ in range(index):
            try:
                temp_node = temp_node.next
            except:
                raise ValueError("Index Out Of Range")
        return temp_node.value 
    
    def set(self, index, value):
        if self.head is None:
            raise ValueError("Index Out Of Range") 
        else:
            if index < 0:
                index = self.length + index 
            if index >= self.length or index < 0:
                raise ValueError("Index Out Of Range")
            else:
                temp_node = self.head 
                for _ in range(index):
                    temp_node = temp_node.next 
                temp_node.value = value 
                return True
            
    def pop(self, index = False):
        if index is not False:
            if index < 0:
                index = self.length + index 
            if index < 0 or index >= self.length:
                raise ValueError("Index Out Of Range")
            else:
                if self.length == 1:
                    if index == 0:
                        node = self.head.value
                        self.tail = None 
                        self.head = None
                        self.length -= 1
                        return node
                    else:
                        raise ValueError("pop Not Works On Empty Linked List")
                else:
                    head_node = self.head 
                    poped_node = self.head
                    next_node  = self.head
                    prev_node = self.head
                    if index == self.length - 1:
                        next_node = self.tail 
                        poped_node = self.tail 
                        for _ in range(index-1):
                            prev_node = prev_node.next
                    elif index == 0:
                        prev_node = self.head 
                        for _ in range(index+1):
                            next_node = next_node.next 
                    else:
                        for _ in range(index+1):
                            next_node = next_node.next 

                        for _ in range(index):
                            poped_node = poped_node.next 
                        for _ in range(index-1):
                            prev_node = prev_node.next
                    if head_node.value == poped_node.value:
                        self.head = next_node
                        head_node.next = None 
                        self.length -= 1
                        return poped_node.value
                    elif next_node.value == poped_node.value:

                        self.tail = prev_node 
                        self.tail.next = None 
                        self.length -= 1
                        return poped_node.value
                    else:
                        prev_node.next = next_node 
                        poped_node.next = None 
                        self.length -= 1
                        return poped_node.value
        else:
            if self.length == 1 and index == 0:
                node = self.head
                self.tail= None 
                self.head = None
                self.length -= 1
                return node.value
            else:
                if self.tail.value is not None:
                    poped_node = self.tail
                    temp_node = self.head 
                    try:
                        while temp_node.next is not self.tail:
                        
                            temp_node = temp_node.next 
                    except:
                        raise ValueError("pop Not Works On Empty Linked List")
                    self.tail = temp_node
                    self.tail.next = None 
                    self.length -= 1 
                    return poped_node.value
                else:
                    raise ValueError("pop Not Works On Empty Linked List")
                
    def remove(self, value):
        index = self.index(value)
        self.pop(index)

    def delete(self):
        self.head = None 
        self.tail = None 
        self.length = 0 
    
    def reverse(self):
        ks = self.traves()
        self.delete()
        for i in ks:
            self.prepend(i)
    
    def deleteDuplicates(self):
        current = self.head
       
        while current is not None and current.next is not None:
            if current.value == current.next.value:
                current.next = current.next.next 
            else:
                current = current.next
    
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head
    
        
        
        
    



my_linked_list = LinkedList()

my_linked_list.append(7)
my_linked_list.append(10)
my_linked_list.reverse()
# my_linked_list.prepend(19)
# my_linked_list.insert(1, 45)
# my_linked_list.insert(2, 50)
# print(my_linked_list)
# print(my_linked_list.index(9))
# print(my_linked_list.get(1))
# print(my_linked_list.set(2, 12))
# print(my_linked_list.pop())
# print(my_linked_list.pop(0))
# print(my_linked_list)
# my_linked_list.remove(45)
# print(my_linked_list)
# my_linked_list.reverse()
# my_linked_list.append(7)
# my_linked_list.append(7)
# my_linked_list.deleteDuplicates()
print(my_linked_list)