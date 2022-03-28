
#########################################################################
#### Implementation of low memory NLP using the Markov Chain Concept ####
#########################################################################


import random


# Define the graph in terms of vertices
class Vertex(object):

    def __init__(self, value):  # value represents the word 
        self.value = value
        self.adjacent = {}      # dictionary that keeps track of which vertices are connected to this vertex, along w weight(i.e. no of occurrences)
        self.neighbours = []
        self.neighbours_weights = []
        

    def add_edge_to(self, vertex, weight=0):    # used to add an adjacent vertex to this vertex
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):   # if the word is already adjacent, we need to increment the weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1    # if word is already in adjacent, the weight is return, else 0. We add 1 to increment

    def get_adjacent_nodes(self):
        pass

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbours.append(vertex)          # we append the adjacent vertex to then list of neighbours
            self.neighbours_weights.append(weight)   # we append the weight of the vertex to the weight list


    def next_word(self):    # randomly select the next word BASED ON WEIGHTS
        return random.choices(self.neighbours, weights=self.neighbours_weights)[0]



# Now we require a way to put together the above vertex representation into a graph

class Graph(object):
    def __init__(self):
        self.vertices = {}      # string to vertex mapping

    def get_vertex_values(self):
        # returns all possible words
        return set(self.vertices.keys())

    def add_vertex(self, value):    # whenever we encounter a new word, we can add that to our graph
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):    # if we want to retrieve a vertex using a word
        
        # in case the word we're looking for is not in the graph, we add it to the graph
        if value not in self.vertices:
            self.add_vertex(value)

        return self.vertices[value] # we return the vertex object that the word represents


    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
