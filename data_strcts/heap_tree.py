from typing import Any


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



class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.leftChild = None
        self.rightChild = None 


class binary_heap:
    def __init__(self):
        self.root = None 

    def maintain_heap(self, leafNode, heap_type):
        if leafNode.parent is None:
            return 
        
        if heap_type == "min":
            if leafNode.data < leafNode.parent.data:
                leafNode.data, leafNode.parent.data = leafNode.parent.data, leafNode.data 
                self.maintain_heap(leafNode.parent, heap_type)
        if heap_type == "max":
            if leafNode.data > leafNode.parent.data:
                leafNode.data, leafNode.parent.data = leafNode.parent.data, leafNode.data 
                self.maintain_heap(leafNode.parent, heap_type)

    def balance_tree(self, root, heap_type):
        if root.leftChild is not None and root.rightChild is not None:
            if heap_type == "max":
                max_node = max(root.leftChild.data, root.rightChild.data)
                if root.leftChild.data == max_node:
                    if root.leftChild.data > root.data:
                        root.data, root.leftChild.data = root.leftChild.data, root.data 
                        self.balance_tree(root.leftChild, heap_type)
                    else:
                        return 
                else:
                    if root.rightChild.data > root.data:
                        root.data, root.rightChild.data = root.rightChild.data, root.data 
                        self.balance_tree(root.rightChild, heap_type)
                    else:
                        return 
            else:
                min_node = min(root.leftChild.data, root.rightChild.data)
                if root.leftChild.data == min_node:
                    if root.leftChild.data < root.data:
                        root.data, root.leftChild.data = root.leftChild.data, root.data 
                        self.balance_tree(root.leftChild, heap_type)
                    else:
                        return 
                else:
                    if root.rightChild.data < root.data:
                        root.data, root.rightChild.data = root.rightChild.data, root.data 
                        self.balance_tree(root.rightChild, heap_type)
                    return

        elif root.leftChild is not None and root. rightChild is None:
            if heap_type == "max":
                if root.leftChild.data > root.data:
                    root.data, root.leftChild.data = root.leftChild.data, root.data 
                    return 
                else:
                    return 
            else:
                if root.leftChild.data < root.data:
                    root.data, root.leftChild.data = root.leftChild.data, root.data 
                    return 
                else:
                    return 
        elif root.leftChild is None and root.rightChild is not None:
            if heap_type == "max":
                if root.rightChild.data > root.data:
                    root.data, root.rightChild.data = root.rightChild.data, root.data
                    return 
                return 
            else:
                if root.rightChild.data > root.data:
                    root.data, root.rightChild.data = root.rightChild.data, root.data
                    return 
                return 
        elif root.leftChild is None and root.rightChild is None:
            return 



    def extract_node(self, data, heap_type):
        if self.root == None:
            return 
        que = QueueLinkedList()
        que.enqueue(self.root)

        matched_node = None
        last_node = None
        while not que.isEmpty():
            root = que.dequeue()
            last_node = root.data
            if root.data.data == data:
                matched_node = root.data 
            if root.data.leftChild is not None:
                que.enqueue(root.data.leftChild)
            if root.data.rightChild is not None:
                que.enqueue(root.data.rightChild)
        if matched_node is not None:
            matched_node.data = last_node.data
            if last_node.parent.leftChild == last_node:
                last_node.parent.leftChild = None
            elif last_node.parent.rightChild == last_node:
                last_node.parent.rightChild = None 
            last_node.parent = None
            self.balance_tree(matched_node, heap_type)
            return True 
        return False
    
    def insertNode(self, data, heap_type):
        node = TreeNode(data)
        if self.root is None:
            self.root = TreeNode(data)
        else:
            que = QueueLinkedList()
            que.enqueue(self.root)

            while not que.isEmpty():
                root = que.dequeue()

                if root.data.leftChild is not None:
                    que.enqueue(root.data.leftChild)
                else:
                    
                    node.parent = root.data
                    root.data.leftChild = node 
                    self.maintain_heap(root.data.leftChild, heap_type)
                    
                    return 
                if root.data.rightChild is not None:
                    que.enqueue(root.data.rightChild)
                else:
                    
                    node.parent = root.data
                    root.data.rightChild = node 
                    self.maintain_heap(root.data.rightChild, heap_type)
                    return 
    
    def get_replace(self, old, new_data, root = [], is_node = False):
        if root == []:
            root = self.root
        if root is None:
            return 
        if root.data == old:
            root.data = new_data 
            is_node = root 
            return is_node
        is_node = self.get_replace(old, new_data, root.leftChild, is_node)
        if is_node:
            return is_node
        is_node = self.get_replace(old, new_data, root.rightChild, is_node)
        return is_node


    def replace_node(self, old_data, new_data, heap_type):
        replaced_node = self.get_replace(old_data, new_data)
        if replaced_node.parent is None:
            self.balance_tree(replaced_node, heap_type)
        else:
            if heap_type == "max":
                if replaced_node.data > replaced_node.parent.data:
                    while replaced_node.parent is not None:
                        if replaced_node.data > replaced_node.parent.data:

                            replaced_node.data, replaced_node.parent.data = replaced_node.parent.data, replaced_node.data
                            replaced_node = replaced_node.parent 
                        else:
                            break
                else:
                    self.balance_tree(replaced_node, heap_type)
            else:
                if replaced_node.data < replaced_node.parent.data:
                    while replaced_node.parent is not None:
                        if replaced_node.data < replaced_node.parent.data:
                            replaced_node.data, replaced_node.parent.data = replaced_node.parent.data, replaced_node.data
                            replaced_node = replaced_node.parent
                        else:
                            break
                else:
                    self.balance_tree(replaced_node, heap_type) 

    def preOrderTraversal(self, root = [], level = 0):
        if root == []:
            root = self.root 
        
        if root is None:
            return 
        if root.parent is None:
            print(" " * level + "|-->" + str(root.data) + " "+ "is root node")
        else:
            print(" " * level + "|-->" + str(root.data) + " "+ "with parent " + str(root.parent.data))
        self.preOrderTraversal(root.leftChild, level + 1)
        self.preOrderTraversal(root.rightChild, level + 1 )
    
my_heap = binary_heap()

my_heap.insertNode(20, "min")
my_heap.insertNode(30, "min")
my_heap.insertNode(40, "min")
my_heap.insertNode(50, "min")
my_heap.insertNode(60, "min")
my_heap.insertNode(70, "min")
my_heap.insertNode(80, "min")
my_heap.insertNode(1, "min")
my_heap.insertNode(8, "min")
my_heap.preOrderTraversal()
print("-----------------------------------------------------------------")
print(my_heap.replace_node(80,5, "min"))
print(my_heap.extract_node(1, "min"))
print("-------------------------------------------------------------------")
print(my_heap.extract_node(60, "min"))
my_heap.replace_node(50, 107, "min")
my_heap.insertNode(100, "min")
my_heap.preOrderTraversal()

