from typing import Mapping


class Graph:
    def __init__(self, graph: Mapping[str, Mapping[str, float]]) -> None:
        self.graph = graph
        self.size = len(graph)