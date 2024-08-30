##############################################################
#
#                     bellman-ford.py
#
#
#     Authored by Vedant Modi (vedantmodi.com)
#     29 Aug 2024
#
#
#     Implements Bellman Ford algorithm using Graph class
#
##############################################################

from typing import Mapping

from graph import Graph


class Bellman_Ford(Graph):
    def __init__(self, graph: Mapping[str, Mapping[str, float]]) -> None:
        super().__init__(graph)

    def bellman_ford(self, source):
        # Init single source
        distances = {u: 0x3F3F3F3F for u in self.graph}
        distances[source] = 0

        V = list(self.graph.keys())

        E = {(k, e): w for k, v in self.graph.items() for e, w in v.items()}

        for _ in V:
            for vertices, w in E.items():
                u, v = vertices
                distances[v] = min(distances[v], distances[u] + w)

        for vertices, w in E.items():
            u, v = vertices
            if distances[v] > distances[u] + w:
                distances = [0x3F3F3F3F for _ in V]  # "False"

        return distances

sol = Bellman_Ford(
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

sol.bellman_ford("a")
