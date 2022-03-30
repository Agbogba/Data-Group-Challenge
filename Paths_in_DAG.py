from collections import defaultdict
from ctypes.wintypes import tagMSG
 
# Class to represent a graph
 
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) 
        self.V = vertices  # No. of vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i[0]] == False:
                self.topologicalSortUtil(i[0], visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Print contents of the stack
        #print(stack[::-1])  # return list in reverse order
        return stack[::-1]

    def longestPath(self, s):
        dist = [-10**9 for i in range(self.V)]

        # Initialize distances to all vertices as infinite and
        # distance to source as 0
        dist[s] = 0
        # Stack.append(1)
        Stack = self.topologicalSort()
        # Process vertices in topological order
        while (len(Stack) > 0):
        
            # Get the next vertex from topological order
            u = Stack[0]
            del Stack[0]
    
            # Update distances of all adjacent vertices
            if (dist[u] != -10**9):
                for i in self.graph[u]:
                    
                    if (dist[i[0]] < dist[u] + i[1]):
                        dist[i[0]] = dist[u] + i[1]

    
        calculated_distance = [dist[i] for i in range(self.V)]
        return calculated_distance
              
    def get_the_most_reachable_vertex(self, s):
        longest_paths = self.longestPath(s)
        greatest_path = max(longest_paths)
        return longest_paths.index(greatest_path)


    def add_new_most_reachable_vertex_to_graph(self, s, origin, new_vertex, weight):
        most_reachable_v = self.get_the_most_reachable_vertex(s)
        for source_vertex, adjacents in self.graph.items():
            for adjacent, _ in adjacents:
                if adjacent == most_reachable_v and source_vertex == origin:
                    raise Exception("The new vertex should'nt share an edge with vertices which share an edge with the current most reachable vertex")  
                
        self.graph[origin].append((new_vertex, weight))
        print("The following entry is added to the graph", (origin, new_vertex, weight))



if __name__ == "__main__":

    g = Graph(9)
    g.addEdge(0, 1, 2)
    g.addEdge(0, 2, 4)
    g.addEdge(0, 4, -2)
    g.addEdge(0, 6, 5)
    g.addEdge(0, 5, 1)
    g.addEdge(2, 3, 3)
    g.addEdge(2, 4, 2)
    g.addEdge(3, 8, -4)
    g.addEdge(4, 3, 5)
    g.addEdge(4, 8, 1)
    g.addEdge(4, 7, 2)
    g.addEdge(5, 7, -1)
    g.addEdge(5, 8, -3)
    g.addEdge(6, 7, 6)
    g.addEdge(7, 8, 2)
 
    print("Following is a Topological Sort of the given graph")
    print(g.topologicalSort())


    s = 0
    print("Following are longest distances from source vertex ",s)
    longest_paths = g.longestPath(s)
    print(longest_paths)

    print("Question 1:")
    print("The vertex reacheable by the greatest number of paths is:", g.get_the_most_reachable_vertex(s)) 
    
    # Sorting and printing the paths according to their cost (descending)
    sorted_paths = sorted(longest_paths, reverse=True)
    print("Question 2:")
    print("Sorted paths in descending is:", sorted_paths)
    
    print("Question 3:")
    g.add_new_most_reachable_vertex_to_graph(s,8,9,-1)

    


    