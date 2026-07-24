from collections import deque
from min_heap import MinHeap


class Graph:
    def __init__(self):
        self._adj = {}

    def add_vertex(self, vertex):
        if vertex not in self._adj:
            self._adj[vertex] = []

    def add_edge(self, source, destination, weight):
        self.add_vertex(source)
        self.add_vertex(destination)
        self._adj[source].append((destination, weight))
        self._adj[destination].append((source, weight))

    def vertices(self):
        return list(self._adj.keys())

    def neighbours(self, vertex):
        return self._adj.get(vertex, [])

    def bfs(self, start, max_hops=None):
        visited = {start}
        order = []
        queue = deque([(start, 0)])
        while queue:
            vertex, depth = queue.popleft()
            order.append((vertex, depth))
            if max_hops is not None and depth == max_hops:
                continue
            for neighbour, _weight in self._adj.get(vertex, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, depth + 1))
        return order

    def dfs(self, start):
        visited = set()
        order = []

        def visit(vertex):
            visited.add(vertex)
            order.append(vertex)
            for neighbour, _weight in self._adj.get(vertex, []):
                if neighbour not in visited:
                    visit(neighbour)

        visit(start)
        return order

    def dijkstra(self, source):
        distances = {v: float("inf") for v in self._adj}
        previous = {v: None for v in self._adj}
        distances[source] = 0

        pq = MinHeap()
        pq.push(0, source)
        visited = set()

        while not pq.is_empty():
            dist, vertex = pq.pop()
            if vertex in visited:
                continue
            visited.add(vertex)

            for neighbour, weight in self._adj.get(vertex, []):
                new_dist = dist + weight
                if new_dist < distances[neighbour]:
                    distances[neighbour] = new_dist
                    previous[neighbour] = vertex
                    pq.push(new_dist, neighbour)

        return distances, previous

    @staticmethod
    def build_path(previous, target):
        path = []
        node = target
        while node is not None:
            path.append(node)
            node = previous.get(node)
        path.reverse()
        return path
