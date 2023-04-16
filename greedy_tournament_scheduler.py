
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
    def __init__(self,index=0):
        self.matches = []
        self.index = index

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
a.add_neighbor(e)
a.add_neighbor(h)

b.add_neighbor(c)
b.add_neighbor(e)
b.add_neighbor(f)

c.add_neighbor(d)
c.add_neighbor(f)
c.add_neighbor(g)

d.add_neighbor(g)
d.add_neighbor(h)

e.add_neighbor(f)
e.add_neighbor(h)

f.add_neighbor(g)

g.add_neighbor(h)

gr = Graph([a,b,c,d,e,f,g,h])
gr.add_vertices()

d = Day()
days = [d]



def attempt_schedule(days, match_str):
        


    for x in range(len(days)):
        if(len(days[x].list_matches())!=0):
            contains = False
            print("Checking day {}".format(x))
            for y in days[x].list_matches():

                if match_str[0] in y:
                    print("Team {} contained in {}".format(match_str[0], y))
                    contains = True
                elif match_str[1] in y:
                    print("Team {} contained in {}".format(match_str[1], y))
                    contains = True

            if ((contains)):
                
                if(x==len(days)-1):
                    print("Adding new day")
                    print("Adding match {} to day {}".format(match_str,x+1))
                    days.append(Day(x+1))
                    days[x+1].add_match(match_str)
                    return True
                    
            else:
                print("Adding match {} to day {}".format(match_str,x))
                days[x].add_match(match_str)
                
                return True
                
        else:
            print("Adding match {} to day {}".format(match_str,x))
            days[x].add_match(match_str)
            return True

for v in gr.return_vertices():
    competitor_1 = v.get_nodes()[0]
    competitor_2 = v.get_nodes()[1]

    match_str = v.output()

    scheduled = False

    while(not(scheduled)):
        scheduled = attempt_schedule(days, match_str)

for i in days:
    print("Day {}".format(i.index))
    print(i.list_matches())