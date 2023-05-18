import random
import Graph


def generate_random_graph():
    random_graph = Graph.Graph()
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

new_graph = Graph.Graph()
test = Graph.Graph()
new_graph.graph = {
    0: [(4, 1), (8, 7)],
    1: [(4, 0), (8, 2), (11, 7)],
    2: [(8, 1), (7, 3), (4, 5), (2, 8)],
    3: [(7, 2), (9, 4), (14, 5)],
    4: [(9, 3), (10, 5)],
    5: [(4, 2), (14, 3), (10, 4), (2, 6)],
    6: [(2, 5), (1, 7), (6, 8)],
    7: [(8, 0), (11, 1), (1, 6), (7, 8)],
    8: [(2, 2), (6, 6), (7, 7)]
}
mst = new_graph.prim_mst()
print(mst)
