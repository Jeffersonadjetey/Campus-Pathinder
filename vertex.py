# Name - Jefferson Adjetey
# Date - March 12, 2021
# Purpose - Create a Vertex class

from cs1lib import *

STROKE_WIDTH = 6
VERTEX_RADIUS = 6


class Vertex:

    def __init__(self, name):
        # instance variables
        self.name = name
        self.adj = []
        self.x = None
        self.y = None
        self.back_pointer = None
        self.visited = None
        self.drawn = False

    def __str__(self):
        adj_list = []  # empty list to add the names of each adjacent vertex
        # takes the list of objects and converts them into a list of strings
        for i in self.adj:
            i = i.name
            adj_list.append(i)

        # creates a single string out of the list
        adj = ', '.join(adj_list)

        return self.name + "; " + "Location:" + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + adj

    # draw a vertex
    def draw_vertex(self, r, g, b, rad=VERTEX_RADIUS):
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, rad)

    # draw an edge using the x and y of a given vertex as well as the x and y of the vertex it is being called on
    def draw_edge(self, vertex, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(STROKE_WIDTH)
        draw_line(self.x, self.y, vertex.x, vertex.y)

    # draw edges between a vertex and all of its' adjacent vertices
    def draw_adjacent_edges(self, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(STROKE_WIDTH)
        for adj in self.adj:
            draw_line(self.x, self.y, adj.x, adj.y)