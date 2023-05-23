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


def main():
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
        's': [(5, 'y'), (10, 't')],
        'y': [(3, 't'), (2, 'z'), (9, 'x')],
        'z': [(6, 'x'), (7, 's')],
        't': [(2, 'y'), (1, 'x')],
        'x': [(4, 'z')]
    }

    mst = prim_graph.prim_mst()
    print(f"MST: {mst}")

    dijkstra_paths = dijkstra_graph.dijkstra('s')
    print(f"\nDistances are {dijkstra_paths[0]}\nPaths are {dijkstra_paths[1]}")

    dijkstra = dijkstra_graph.shortest_path('s', 'x')
    print(f"\nShortest distance between s and x is {dijkstra[0]}\nShortest path is {dijkstra[1]}\n")

    section_graph = graph.Graph()
    section_graph.graph = {
        0: [(2, 1), (1, 3), (4, 4)],
        1: [(2, 0), (3, 2), (3, 3), (7, 5)],
        2: [(3, 1), (5, 3), (8, 5)],
        3: [(1, 0), (3, 1), (5, 2), (9, 4)],
        4: [(4, 0), (9, 3)],
        5: [(7, 1), (8, 2)]
    }

    mst = section_graph.prim_mst()
    print(f"MST: {mst}")

    dijkstra_paths = section_graph.dijkstra(4)
    print(f"\nDistances are {dijkstra_paths[0]}\nPaths are {dijkstra_paths[1]}")

    dijkstra = section_graph.shortest_path(4, 5)
    print(f"\nShortest distance between 4 and 5 is {dijkstra[0]}\nShortest path is {dijkstra[1]}\n")


if __name__ == "__main__":
    main()
