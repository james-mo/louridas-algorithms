from graph import Graph, Node

def dijkstra(graph:Graph, start:Node, end:Node):
    nodes = graph.get_nodes()
    distances = dict()
    distances[start] = 0
    for i in nodes:
        if i != start:
            distances[i] = float("inf")
    
    visited = dict()
    for i in nodes:
        visited[i] = False

    previous = dict()
    for i in nodes:
        previous[i] = None
    

    while not all (visited.values()):
        #find the unvisited node with the smallest distance
        current = None
        current_distance = float("inf")
        for i in nodes:
            if not visited[i] and distances[i] < current_distance:
                current = i
                current_distance = distances[i]
        
        print(current.name)
        visited[current] = True
        neighbors = current.get_neighbors()
        for n in neighbors:
            node = n[0]
            if distances[node] > distances[current] + n[1]:
                print("distance to " + node.name + " is " + str(distances[node]) + " and is now " + str(distances[current] + n[1]))
                distances[node] = distances[current] + n[1]
                previous[node] = current

    #reconstruct path
    path = []
    current = end
    while current != start:
        path.append(current.name)
        current = previous[current]
    path.append(start.name)
    path.reverse()
    return path

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

a.add_neighbor(b, 3)
a.add_neighbor(c, 1)
b.add_neighbor(d, 3)
b.add_neighbor(f, 6)
c.add_neighbor(d, 4)
c.add_neighbor(e, 2)
d.add_neighbor(f, 1)
e.add_neighbor(f, 5)
f.add_neighbor(e, 2)

gr = Graph([a,b,c,d,e,f])

print(dijkstra(gr, a, f))

