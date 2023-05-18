import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def primMST(self):
        mst = []
        visited = set()
        heap = []
        startV = next(iter(self.graph))

        visited.add(startV)
        for edge in self.graph[startV]:
            heapq.heappush(heap, edge)

        while len(heap) > 0:
            v, weight = heapq.heappop(heap)
            if v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
                for edge in self.graph[u]:
                    neighbor, neighborWeight = edge
                    heapq.heappush(heap, (neighbor, neighborWeight))


g = Graph()
g.addEdge('A', 'B', 7)
g.addEdge('A', 'C', 8)
g.primMST('A')
