class TreeNode:
    def __init__(self, data, childern = []):
        self.data = data 
        self.childern = childern 

    def __str__(self, level = 0):
        ret = " "  * level +"|_" + str(self.data) + "\n"

        for i in self.childern:
            ret += i.__str__(level + 1)
        return ret 
    
    def addNode(self, TreeNode):
        self.childern.append(TreeNode)

tree = TreeNode("Drinks", [])
cold = TreeNode("cold", [])
hot = TreeNode("hot", [])

tree.addNode(cold)
tree.addNode(hot)

tea = TreeNode("tea", [])
coffee = TreeNode("coffee", [])
hot.addNode(tea)
hot.addNode(coffee)
fanta = TreeNode("fanta", [])
maza = TreeNode("maza", [])
cold.addNode(fanta)
cold.addNode(maza)
print(tree)