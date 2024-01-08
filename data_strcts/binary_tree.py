
import Queue_linked_list as q 

class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.leftNode = None
        self.rightNode = None 


class Tree:
    def __init__(self):
        self.root = None 

    def preOrderTraversal(self, rootNode, level = 0):
        if not rootNode:
            return 
        print(" "*level + "|_" +rootNode.data)
        self.preOrderTraversal(rootNode.leftNode, level + 1)
        self.preOrderTraversal(rootNode.rightNode, level + 1)
    
    def postOredrTraversal(self, rootNode, level = 0):
        if not rootNode:
            return 
        self.postOredrTraversal(rootNode.leftNode, level + 1)
        self.postOredrTraversal(rootNode.rightNode, level + 1)
        print(" "*level + "|_" +rootNode.data)


    def inOrderTraversal(self, rootNode, level = 0):
        if not rootNode:
            return 
        self.inOrderTraversal(rootNode.leftNode, level + 1)
        print(" "*level + "|_" +rootNode.data)
        self.inOrderTraversal(rootNode.rightNode, level + 1)

    def levelOrder(self, rootNode):
        queue = q.QueueLinkedList()
        queue.enqueue(rootNode)

        while not(queue.isEmpty()):
            root = queue.dequeue()
            print(root.data.data)

            if root.data.leftNode is not None:
                queue.enqueue(root.data.leftNode)
            
            if root.data.rightNode is not None:
                queue.enqueue(root.data.rightNode)

    def insertNode(self, data, root = []):
        if root == []:
            root = self.root
        node = TreeNode(data)
        if root is not None:
            queue = q.QueueLinkedList()
            queue.enqueue(self.root)

            while not queue.isEmpty():
                root = queue.dequeue()
                if root.data.leftNode is not None:
                    queue.enqueue(root.data.leftNode)
                else:
                    root.data.leftNode = node 
                    return 

                if root.data.rightNode is not None:
                    queue.enqueue(root.data.rightNode)
                else:
                    root.data.rightNode = node 
                    return 
            
            

        else:
            self.root = node
    
    def delete_node(self, data):
        if self.root.data == data:
            self.root = None
            return 
        else:
            queue = q.QueueLinkedList()
            queue.enqueue(self.root)

            while not queue.isEmpty():
                root = queue.dequeue()
                if root.data.leftNode.data == data:
                    root.data.leftNode = None
                    return 
                elif root.data.rightNode.data == data:
                    root.data.rightNode = None 
                    return 
                if root.data.leftNode is not None:
                    queue.enqueue(root.data.leftNode)
                if root.data.rightNode is not None:
                    queue.enqueue(root.data.rightNode)

    def delete(self):
        self.root = None





        

tree = Tree()
tree.insertNode("Drinks")  
tree.insertNode("cold")  
tree.insertNode("hot")  
tree.insertNode("fanta")
tree.insertNode("limka")
tree.insertNode("tea")
tree.insertNode("coffee")
tree.insertNode("red_fanta")
tree.delete_node("coffee")

tree.preOrderTraversal(tree.root)
print("-------------------------------------------")
tree.postOredrTraversal(tree.root)
print("-------------------------------------------------")
tree.inOrderTraversal(tree.root)
print("-------------------------------------------------")
tree.levelOrder(tree.root)


    