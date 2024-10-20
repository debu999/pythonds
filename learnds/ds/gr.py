from typing import Dict, List


class Graph:
    def __init__(self):
        self.adj_list: Dict[int, List] = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph if it does not already exist.

        Args:
            vertex: The vertex to be added to the graph.

        Returns:
            bool: True if the vertex was successfully added, False otherwise.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False


def add_edge(self, v1, v2):
    """
    Adds a new edge between two vertices in the graph's adjacency list.

    Args:
        v1: The first vertex of the edge.
        v2: The second vertex of the edge.

    Returns:
        bool: True if the edge was successfully added, False otherwise.
    """
    if v1 in self.adj_list and v2 in self.adj_list:
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return True
    return False


def remove_edge(self, v1, v2):
    """
    Removes a edge between two vertices in the graph's adjacency list.

    Args:
        v1: The first vertex of the edge.
        v2: The second vertex of the edge.

    Returns:
        bool: True if the edge was successfully added, False otherwise.
    """
    if v1 in self.adj_list and v2 in self.adj_list:
        self.adj_list[v1].remove(v2)
        self.adj_list[v2].remove(v1)
        return True
    return False


def remove_vertex(self, vertex):
    if vertex in self.adj_list:
        # Remove the vertex from the graph
        other_vertices = self.adj_list[vertex]
        for v in other_vertices:
            print(self.adj_list[v])
            self.adj_list[v].remove(vertex)
        self.adj_list.pop(vertex)
        return True
    else:
        return False


my_graph = Graph()

my_graph.add_vertex("A")

my_graph.print_graph()


"""
    EXPECTED OUTPUT:
    ----------------
    A : []

"""
