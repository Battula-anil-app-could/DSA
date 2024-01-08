class Graph:
    def __init__(self):
        self.dic = {}
    
    def print_graph(self):
        for k,v in self.dic.items():
            print(k, ": ", v)
    
    def add_vertex(self, vertex):
        if vertex not in self.dic.keys():
            self.dic[vertex] = []
    
    def add_edge(self, v1, v2):
        if v1 in self.dic.keys() and v2 in self.dic.keys(): 
            if v2 not in self.dic[v1]:
                self.dic[v1].append(v2)

    def remove_edge(self, v1, v2):
        if v1 in self.dic.keys() and v2 in self.dic.keys():
            if v1 in self.dic[v2] and v2 in self.dic[v1]:
                self.dic[v1].remove(v2)
                self.dic[v2].remove(v1)
            elif v1 in self.dic[v2]:
                self.dic[v2].remove(v1)
            elif v2 in self.dic[v1]:
                self.dic[v1].remove(v2)
    
    def bfs(self):
        marked = []
        for k, v in self.dic.items():
            if k not in marked:
                print(k)
                marked.append(k)
            for i in v:
                if i not in marked:
                    print(i)
                    marked.append(i)

    def dfs(self, vertex):
        visited = set()
        stack = [vertex]

        while stack:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)
            for i in self.dic[current]:
                if i not in visited:
                    stack.append(i)
    
    def topological_util(self, v, visited, stack):
        visited.append(v)

        for i in self.dic[v]:
            if i not in visited:
                self.topological_util(i, visited, stack)
        
        stack.insert(0, v)
    
    def topological___sort(self):
        visited = []
        stack = []
        for k,v in self.dic.items():
            if k not in visited:
                self.topological_util(k, visited, stack)
        
        print(stack)

my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.add_vertex("F")
my_graph.add_vertex("G")
my_graph.add_vertex("H")
my_graph.add_edge("A", "C")
my_graph.add_edge("C", "E")
my_graph.add_edge("E", "H")
my_graph.add_edge("E", "F")
my_graph.add_edge("F", "G")
my_graph.add_edge("B", "C")
my_graph.add_edge("B", "D")
my_graph.add_edge("D", "E")
my_graph.print_graph()
print("------------------------------------------------------------------")
my_graph.bfs()
print("------------------------------------------------------------------")
my_graph.topological___sort()