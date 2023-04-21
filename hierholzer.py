# hierholzer algorithm to find an eulerian path in a graph

from graph import Graph, Node
import random

def hierholzer(graph:Graph,start:Node=None):
    nodes = graph.get_nodes()
    path = []
    visited = dict()
    for i in nodes:
        visited[i] = False

    used_edges = dict()
    for i in nodes:
        n = i.get_neighbors()
        for j in n:
            used_edges[(i,j)] = False


    if(start==None):
        start = random.choice(nodes)
    path.append(start)
    visited[start] = True
    current = random.choice(start.get_neighbors())
    while current != start:
        path.append(current)
        visited[current] = True

        for i in current.get_neighbors():
            if not visited[i]:
                used_edges[(current,i)] = True
                current = i
                break
    
    # as long as there exists a node in the path
    # which is part of an edge that has not been used,
    # start another path from that node, using unused edges,
    # until we return to the start node, and then splice
    # the new path into the old path

    while True:

        # find the first node in the path that is part of an unused edge
        for i in range(len(path)):
            if not used_edges[(path[i-1],path[i])]:
                start = path[i]
                break
        else:
            break

        # find the first unused edge
        for i in start.get_neighbors():
            if not used_edges[(start,i)]:
                current = i
                break

        # find the path
        new_path = []
        while current != start:
            new_path.append(current)
            visited[current] = True

            for i in current.get_neighbors():
                if not visited[i]:
                    used_edges[(current,i)] = True
                    current = i
                    break

        # splice the new path into the old path
        path = path[:i] + new_path + path[i:]


aa = Node("AA")
at = Node("AT")
tg = Node("TG")
gg = Node("GG")
gc = Node("GC")
cg = Node("CG")
gt = Node("GT")
ca = Node("CA")

aa.add_neighbor(at)
at.add_neighbor(tg)
tg.add_neighbor(gg)
tg.add_neighbor(gc)
gg.add_neighbor(gc)
gc.add_neighbor(cg)
gc.add_neighbor(ca)
cg.add_neighbor(gt)
gt.add_neighbor(tg)

g = Graph([aa,at,tg,gg,gc,cg,gt,ca])
print(hierholzer(g))

