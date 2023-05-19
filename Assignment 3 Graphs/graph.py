import heapq
import sys


class Graph:
    def __init__(self, is_directed=False):
        # u : [(weight,v),.....]
        self.graph = {}
        self.directed = is_directed

    def add_edge(self, u, v, weight):
        # u -> v if graph is directed
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((weight, v))
        if self.directed:
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

    def dijkstra(self, starting_vertex):
        if starting_vertex not in self.graph:
            return

        visited = set()  # keep track of visited vertices
        heap = []  # priority heap to get the shortest distance
        distances = {}  # dictionary to store shortest distance between starting vertex and all other vertices
        path = {}  # dictionary that stores paths from starting vertex to all other vertices

        # initialize with max distance at every vertex
        for vertex in self.graph:
            distances[vertex] = sys.maxsize
            path[vertex] = []

        distances[starting_vertex] = 0

        heapq.heappush(heap, (0, starting_vertex))

        while len(heap) > 0:
            weight, vertex = heapq.heappop(heap)

            if vertex in visited:
                continue

            visited.add(vertex)

            for edge in self.graph[vertex]:
                # edge[0] is the weight and edge[1] is the neighbor
                if distances[vertex] + edge[0] < distances[edge[1]]:
                    distances[edge[1]] = distances[vertex] + edge[0]
                    path[edge[1]] = path[vertex] + [vertex]
                    heapq.heappush(heap, (distances[edge[1]], edge[1]))

        return distances, path

    def shortest_path(self, starting_vertex, destination_vertex):
        if starting_vertex not in self.graph or destination_vertex not in self.graph:
            return
        distances, path = self.dijkstra(starting_vertex)
        return distances[destination_vertex], path[destination_vertex] + [destination_vertex]
