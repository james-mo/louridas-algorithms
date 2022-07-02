
class Vertex:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def get_nodes(self):
        return [self.node1, self.node2]

    def output(self):
        str = ""
        str += self.node1.output()
        str += self.node2.output()

        return ''.join(sorted(str))

class Day:
    def __init__(self):
        self.matches = []

    def add_match(self, match_string):
        self.matches.append(match_string)
    
    def list_matches(self):
        return self.matches


class Graph:
    
    def __init__(self, nodes):
        self.nodes = nodes
        self.vertices = []

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
    
    def return_vertices(self):
        return self.vertices


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    
    def add_neighbor(self, node):
        self.neighbors.append(node)
        if(not(self in node.get_neighbors())):
            node.add_neighbor(self)

    def get_neighbors(self):
        return self.neighbors

    def output(self):
        return self.name
    
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")

a.add_neighbor(b)
a.add_neighbor(d)
a.add_neighbor(h)
a.add_neighbor(e)

d.add_neighbor(h)
d.add_neighbor(g)
d.add_neighbor(c)

h.add_neighbor(g)
h.add_neighbor(e)

e.add_neighbor(b)
e.add_neighbor(f)

f.add_neighbor(g)
f.add_neighbor(c)
f.add_neighbor(b)

b.add_neighbor(c)

c.add_neighbor(g)

gr = Graph([a,b,c,d,e,f,g,h])
gr.add_vertices()

d = Day()
days = [d]

def attempt_schedule(days, match_str):

        for x in range(len(days)):
            if(len(days[x].list_matches())!=0):
                contains = False
                for y in days[x].list_matches():

                    if match_str[0] in y:
                        contains = True
                    elif match_str[1] in y:
                        contains = True

                if ((contains)):

                    if(x==len(days)-1):
                        days.append(Day())
                        
                else:
                    days[x].add_match(match_str)
                    
                    return True
                    
            else:
                days[x].add_match(match_str)
                return True

for v in gr.return_vertices():
    competitor_1 = v.get_nodes()[0]
    competitor_2 = v.get_nodes()[1]

    match_str = v.output()
    print(match_str)

    scheduled = False

    while(not(scheduled)):
        scheduled = attempt_schedule(days, match_str)

for i in days:
    print(i.list_matches())