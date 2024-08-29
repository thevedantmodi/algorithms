##############################################################
#
#                     main.py
#
#
#     Authored by Vedant Modi (vedantmodi.com)
#     27 Aug 2024
#
#
#     Graph algo implementations w adj list
#
##############################################################


from heapq import heappop, heappush


class Graph:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.size = len(graph)

    def dijkstra(self, source):
        # Init single source
        distances = {u: 0x3F3F3F3F for u in self.graph}
        distances[source] = 0

        queue = [(0, source)]

        seen = set()

        while queue:
            ud, u = heappop(queue)

            if u in seen:
                continue

            seen.add(u)

            for v, vd in self.graph[u].items():
                relax = ud + vd
                if relax < distances[v]:
                    distances[v] = relax
                    heappush(queue, (relax, v))

        # SSSP is optimal way to answer shortest path between u,v
        return distances


# Outer dict: vertex
# Inner dict: edge
# [[(,)]]

sol = Graph(
    {
        "a": {"b": 4, "h": 8},
        "b": {"a": 4, "h": 11, "c": 8},
        "c": {"f": 4, "i": 2, "b": 8, "d": 7},
        "d": {"f": 14, "c": 7, "e": 9},
        "e": {"f": 10, "d": 9},
        "f": {"c": 4, "g": 2, "e": 10, "d": 14},
        "g": {"i": 6, "h": 1, "f": 2},
        "h": {"i": 7, "a": 8, "g": 1},
        "i": {"h": 7, "c": 2, "g": 6},
    }
)
print(sol.dijkstra("a"))
