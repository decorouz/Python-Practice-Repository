"""
Given a list of words, determine whether the words can be 
chained to form a circle. 
A word X can be placed in front of another word Y in a circle 
if the last character of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', touch', 'tunic'] 
can form the following 
circle: chair --> racket --> touch --> height --> tunic --> chair

"""
from collections import defaultdict

CHARS = 26


class Graph:
    """A graph use to represent an undirected graph."""

    def __init__(self, vertices) -> None:
        """
        Parameters
        ----------
        vertices: int
            The number of vertex
        """
        self.vertices = vertices
        self.adj = defaultdict(list)
        self.inp = [0] * vertices

    def add_edge(self, v, u):
        """Add an edge to the graph."""
        self.adj[v].append(u)
        self.inp[u] += 1

    def is_sc(self):
        """Check if the graph is Eulerian or not."""
        # mark all vertices as unvisited.
        visited = [False] * self.vertices

        # find the vertex with non-zero degree
        non_zero_deg_vertex = 0
        for non_zero_deg_vertex in range(self.vertices):
            # find the first vertex with nonzero degree vertex
            if len(self.adj[non_zero_deg_vertex]) > 0:
                break

        self.DFSUtil(non_zero_deg_vertex, visited)

        # If DFS traversal doesn't visit all vertices, then return false.
        for i in range(self.vertices):
            if len(self.adj[i]) > 0 and visited[i] is False:
                return False

        gr = self.get_transposed()  # Create a reversed graph

        for i in range(self.vertices):
            # Mark all vertices as not visited (second DFS)
            visited[i] = False

        # Do DFS for reversed graph starting from first vertex.
        # Starting Vertex must be same starting point of first DFS
        gr.DFSUtil(n, visited)

        for i in range(self.vertices):
            # If all vertices are not visited on the DFS, then return False
            if len(self.adj[i]) > 0 and visited[i] is False:
                return False
        return True

    def is_eulerian_cycle(self):
        """Evaluate to true or false.

        if the directed graph has an eulerian cycle, otherwise returns false.
        """
        # Check if all non-zero degree vertices are connected
        if self.is_sc() is False:
            return False

        for i in range(self.vertices):
            # Check if in degree and out degree of every vertex is same
            if len(self.adj[i]) != self.IN[i]:
                return False
        return True

    def DFSUtil(self, v, visited):
        # Recur for all the vertices adjacent to this vertex
        visited[v] = True  # Mark the current node as visited and print it

        for i in range(len(self.adj[v])):
            if not visited[self.adj[v][i]]:
                self.DFSUtil(self.adj[v][i], visited)

    def get_transposed(self):
        g = Graph(self.vertices)
        for v in range(self.vertices):
            for i in range(len(self.adj[v])):
                g.adj[self.adj[v][i]].append(v)
                g.IN[v] += 1
        return g


# This function takes an of strings and returns true
# if the given array of strings can be chained to
# form cycle
def can_be_chained(arr, n):
    # Create a graph with 'alpha' edges
    g = Graph(CHARS)

    # Create an edge from first character to last character
    # of every string
    for i in range(n):
        s = arr[i]
        g.add_edge(ord(s[0]) - ord("a"), ord(s[len(s) - 1]) - ord("a"))

    # The given array of strings can be chained if there
    # is an eulerian cycle in the created graph
    return g.is_eulerian_cycle()


# Driver program
if __name__ == "main":
    arr1 = ["for", "geek", "rig", "kaf"]
    n1 = len(arr1)
    if can_be_chained(arr1, n1):
        print("Can be chained")
    else:
        print("Cant be chained")

    arr2 = ["chair", "height", "racket", "touch", "tunic"]
    n2 = len(arr2)
    if can_be_chained(arr2, n2):
        print("Can be chained")
    else:
        print("Can't be chained")
