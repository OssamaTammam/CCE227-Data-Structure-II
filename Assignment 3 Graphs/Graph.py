import heapq


class Graph:
    def __init__(self):
        # u : [(weight,v),.....]
        self.graph = {}
        self.no_vertices = 0

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
            self.no_vertices += 1
        if v not in self.graph:
            self.graph[v] = []
            self.no_vertices += 1
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))

    def print_graph(self):
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                print(f"{vertex}->{edge[1]} with weight {edge[0]}")

    def prim_mst(self):
        starting_vertex = next(iter(self.graph))
        visited = set()
        heap = []
        mst = []

        visited.add(starting_vertex)
        for edge in self.graph[starting_vertex]:
            heapq.heappush(heap, (edge[0], starting_vertex, edge[1]))

        while len(heap) > 0:
            weight, u, v = heapq.heappop(heap)

            if v in visited:
                continue

            visited.add(v)
            mst.append((u, v, weight))

            for edge in self.graph[v]:
                # v is starting_vertex and edge[1] is its neighbor
                heapq.heappush(heap, (edge[0], v, edge[1]))

        return mst
