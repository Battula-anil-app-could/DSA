
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.leftChild = None 
        self.rightChild = None 

class binary_search_tree:
    def __init__(self):
        self.root = None 

    
    def preOrderTraversal(self, rootNode, level = 0):
        if rootNode is None:
            return 
        else:
            print(" " * level + "|_" + str(rootNode.data))
            self.preOrderTraversal(rootNode.leftChild, level +1)
            self.preOrderTraversal(rootNode.rightChild, level + 1)

    

    def insertNode(self, data, root = []):
        if root == []:
            root = self.root
        node = TreeNode(data)
        if self.root is None:
            self.root = node 
        else:
            if root.data > data:
                if root.leftChild is None:
                    root.leftChild = node 
                else:
                    self.insertNode(data, root.leftChild)
            else:
                if root.rightChild is None:
                    root.rightChild = node 
                else:
                    self.insertNode(data, root.rightChild)

    def searchNode(self, node, root = [], level = 0):
        if root == []:
            root = self.root 
        
        if root is None:
            return "Tree not having this node: " + str(node.data)
        if root.data == node.data:
            return str(root.data) + " " + "with level of " + str(level+1)
        elif node.data < root.data:
            return self.searchNode(node, root.leftChild, level + 1)
        else:
            return self.searchNode(node, root.rightChild, level + 1)
        

    
    def search_with_level(self, data):
        node = TreeNode(data)

        if self.root is None:
            return False
        result = self.searchNode(node)
        return result
    
    def delete_node(self, data, root = []):
        if root == []:
            root = self.root 
        if root is None:
            return "node not having"
        if root.leftChild is not None:
            if root.leftChild.data == data:
                root.leftChild = None
                return True 
        elif root.rightChild is not None:
            if root.rightChild.data == data:
                root.rightChild = None
                return True
        else:
            if data < root.data:
                return self.delete_node(data, root.leftChild)
            else:
                return self.delete_node(data, root.rightChild)
            


mytree = binary_search_tree()
mytree.insertNode(70)
mytree.insertNode(50)
mytree.insertNode(80)
mytree.insertNode(40)
mytree.insertNode(75)
mytree.insertNode(90)
mytree.insertNode(75)
mytree.insertNode(70)
print(mytree.delete_node(76))
mytree.preOrderTraversal(mytree.root)
print(mytree.search_with_level(76))
print(mytree.search_with_level(40))
