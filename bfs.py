# Name - Jefferson Adjetey
# Date - March 12, 2021
# Purpose - Write a function to perform a breadth-first search

from load_graph import load_graph
from vertex import Vertex
from collections import deque

# grab the dictionary of vertex objects

vertex_dict = load_graph("dartmouth_graph.txt")


def run_bfs(start, goal):
    frontier = deque('')  # create the deque for the frontier
    backpointer = {}  # create an empty dictionary for the backpointers

    frontier.append(start)  # start vertex added to the frontier
    backpointer[start] = None  # add the start vertex to the dictionary

    while frontier:  # run while frontier is empty

        current_vertex = frontier.popleft()  # current vertex is removed from the deque

        for adjacent in current_vertex.adj:  # calls each adjacent vertex for the current vertex
            if adjacent in backpointer:
                continue

            else:
                frontier.append(adjacent)  # adds adjacent vertices to the frontier
                backpointer[adjacent] = current_vertex  # adds adjacent vertices to the dictionary

        if goal in backpointer:  # if goal vertex is in the dictionary, break
            break

    if goal in backpointer:  # runs if the goal vertex is in the dictionary

        current_vertex = goal  # sets current vertex to goal, initializes an empty list for the path
        path = []
        while current_vertex is not None:
            # backtracks through the dictionary all the way up to the start vertex
            path.append(current_vertex)
            # adds the vertices on the most direct path to the start
            current_vertex = backpointer[current_vertex]

        return path  # returns the list
