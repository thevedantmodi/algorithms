##############################################################
#
#                     floyd-warshall.py
#
#
#     Authored by Vedant Modi (vedantmodi.com)
#     30 Aug 2024
#
#
#     Floyd Watshall Implementation
#
##############################################################

from typing import Mapping

from graph import Graph


class Floyd_Warshall(Graph):
    def __init__(self, graph: Mapping[str, Mapping[str, float]]) -> None:
        super().__init__(graph)

    def floyd_warshall(self):
        V = list(self.graph.keys())
        D = {i: {j: 0x3F3F3F3F for j in V} for i in V}  # adj dict matrix

        for i in V:
            D[i][i] = 0
            for j in self.graph[i]:
                D[i][j] = self.graph[i][j]

        for k in V:
            for i in V:
                for j in V:
                    # take the k steps between two nodes, or default to prev
                    # state, and don't improve at all
                    D[i][j] = min(D[i][k] + D[k][j], D[i][j])

        return D


sol = Floyd_Warshall(
    {
        "1": {"2": 3, "3": 8, "5": -4},
        "2": {"4": 1, "5": 7},
        "3": {"2": 4},
        "4": {"1": 2, "3": -5},
        "5": {"4": 6},
    }
)

sol.floyd_warshall()
