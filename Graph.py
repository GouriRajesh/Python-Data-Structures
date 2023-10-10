''' We are making use of an adjacency list to represent graphs as it is more efficient 
overall compared to an adjacency matrix '''

class Graph :
    def __init__(self) :
        # Dictionary is used to represent an adjacency list
        self.adj_list = {}

    def print_adj_list(self) :
        print('The adjacency list for graph is :')
        for vertex in self.adj_list :
            print(vertex , ':', self.adj_list[vertex])
    
    def add_vertex(self, vertex) :
        # Prevent insertion of duplicate vertices
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2) :
        # Add edge only if vertices are present in the graph
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2) 
            self.adj_list[v2].append(v1) 
            return True
        return False

    def remove_edge(self, v1, v2):
        # Remove edge only if vertices are present in the graph
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                # Edge exists between vertices
                self.adj_list[v1].remove(v2) 
                self.adj_list[v2].remove(v1) 
            except ValueError:
                # Edge does not exist between vertices
                pass
            return True
        return False
    
    def remove_vertex(self, vertex) :
        # Remove vertex only if vertex is present in the graph
        if vertex in self.adj_list.keys():

            # Step 1 : Remove vertex from all edges (loop through vertex list only as graph is bidirectional)
            for edge_vertex in self.adj_list[vertex]:
                self.adj_list[edge_vertex].remove(vertex)

            # Step 2 : Remove vertex
            del self.adj_list[vertex]

            return True
        return False
        

#------------------- PRINT OPERATIONS -------------------
# Create a new graph
my_graph = Graph()

# Add vertices to the graph
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.add_vertex('E')

# Print the adjacency list
my_graph.print_adj_list()

# Add edges between the vertices
my_graph.add_edge('A','B')
my_graph.add_edge('B','C')
my_graph.add_edge('C','A')
my_graph.add_edge('D','B')
my_graph.print_adj_list()

# Remove edges between the vertices
my_graph.remove_edge('A','B')
my_graph.remove_edge('D','A')
my_graph.print_adj_list()

# Remove vertex
my_graph.remove_vertex('C')
my_graph.print_adj_list()