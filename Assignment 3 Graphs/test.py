import random
import graph


def generate_random_graph():
    random_graph = graph.Graph()
    no_vertices = random.randint(5, 15)
    for vertex in range(no_vertices):
        no_edges = random.randint(2, 4)
        for _ in range(no_edges):
            weight = random.randint(1, 100)
            neighbor = random.randint(0, no_vertices - 1)
            random_graph.add_edge(vertex, neighbor, weight)
    return random_graph


# new_graph = generate_random_graph()
# new_graph.print_graph()
# mst = new_graph.prim_mst()
# print(mst)

# new_graph = Graph.Graph()
# test = Graph.Graph()
# new_graph.graph = {
#     0: [(4, 1), (8, 7)],
#     1: [(4, 0), (8, 2), (11, 7)],
#     2: [(8, 1), (7, 3), (4, 5), (2, 8)],
#     3: [(7, 2), (9, 4), (14, 5)],
#     4: [(9, 3), (10, 5)],
#     5: [(4, 2), (14, 3), (10, 4), (2, 6)],
#     6: [(2, 5), (1, 7), (6, 8)],
#     7: [(8, 0), (11, 1), (1, 6), (7, 8)],
#     8: [(2, 2), (6, 6), (7, 7)]
# }
# dist, path = new_graph.shortest_path(0, 3)
# print(dist)
# print(path)

prim_graph = graph.Graph()
prim_graph.graph = {
    'a': [(4, 'b'), (8, 'h')],
    'b': [(4, 'a'), (11, 'h'), (8, 'c')],
    'c': [(8, 'b'), (2, 'i'), (4, 'f'), (7, 'd')],
    'd': [(7, 'c'), (14, 'f'), (9, 'e')],
    'e': [(9, 'd'), (10, 'f')],
    'f': [(10, 'e'), (14, 'd'), (4, 'c'), (2, 'g')],
    'g': [(2, 'f'), (6, 'i'), (1, 'h')],
    'h': [(1, 'g'), (7, 'i'), (11, 'b'), (8, 'a')],
    'i': [(6, 'g'), (7, 'h'), (2, 'c')]
}

dijkstra_graph = graph.Graph(True)
dijkstra_graph.graph = {
    0: [(5, 5), (10, 8)],
    5: [(3, 8), (2, 7), (9, 9)],
    7: [(6, 9), (7, 0)],
    8: [(2, 5), (1, 9)],
    9: [(4, 7)]
}

mst = prim_graph.prim_mst()
print(mst)

dijkstra = dijkstra_graph.shortest_path(0, 9)
print(dijkstra)
