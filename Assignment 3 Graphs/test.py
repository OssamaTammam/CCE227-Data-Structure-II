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



