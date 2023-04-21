class Vertex:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def get_nodes(self):
        return [self.node1, self.node2]

    def output(self):
        str = ""
        str += self.node1.output()
        str += self.node2[0].output()

        return ''.join(sorted(str))

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    
    def add_neighbor(self, node, weight=1):
        self.neighbors.append([node,weight])

    def get_neighbors(self):
        return self.neighbors

    def output(self):
        return self.name

class Graph:
    
    def __init__(self, nodes):
        self.nodes = nodes
        self.vertices = []
        self.add_vertices()

    def add_vertices(self):

        for n in self.nodes:
            neighbors = n.get_neighbors()
            for ni in neighbors:
                v = Vertex(n,ni)
                contains = False
                for vi in self.vertices:
                    if v.output() == vi.output():
                        contains = True
                if(not(contains)):
                    self.vertices.append(v)

    def size(self):
        return len(self.vertices)
    
    def return_vertices(self):
        return self.vertices

    def get_node(self, n:int) -> Node:
        return self.nodes[n]
    
    def get_nodes(self) -> list[Node]:
        return self.nodes


