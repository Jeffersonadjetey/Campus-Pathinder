# Name - Jefferson Adjetey
# Date - March 12, 2021
# Purpose - Write a program to plot the optimal path between a list of vectors

from cs1lib import *
from load_graph import load_graph
from bfs import run_bfs
from vertex import Vertex

# constant variables for frame
FRAME_WIDTH = 1012
FRAME_HEIGHT = 811

# variables to record the state of the map
map_draw = False
vertices_draw = False
starter_set = False
edges_draw = False
bfs = False
goal_set = False


# variable that records clicks
isClicked = False

# variables to hold the value of the starter and goal vertices
starter = None
goal = None

# variables to hold the x and y values of the starter and goal vertices
starter_x, starter_y = 0, 0
goal_x, goal_y = 0, 0

# variables to record the position of the mouse
x = 0
y = 0
x1 = 0
y1 = 0

# grab the dictionary of vertex objects
vertex_dict = load_graph("dartmouth_graph.txt")


#  vertices on the map
def draw_vertices():
    for vertex in vertex_dict:
        if not vertex_dict[vertex].drawn:  # if the vertex is not drawn
            vertex_dict[vertex].draw_vertex(0, 0, 1)
            vertex_dict[vertex].drawn = True


# draw the edges on the map
def draw_edges():
    for vertex in vertex_dict:
        vertex_dict[vertex].draw_adjacent_edges(0, 0, 1)


# record if mouse is pressed
def mousedown(mx, my):
    global x1, y1, isClicked
    isClicked = True
    x1 = mx
    y1 = my


# record mouse release
def mouseup(mx, my):
    global isClicked, x, y
    isClicked = False


def set_starter():
    global starter_set, starter_x, starter_y, starter
    # if the starter vertex is not drawn and the mouse is clicked, continue with the function
    if starter_set is False and isClicked is True:
        for vertex in vertex_dict:

            # if the mouse click is on a vertex, draw the vertex in red
            if x1 in range(vertex_dict[vertex].x - 25, vertex_dict[vertex].x + 25) and y1 in range(
                    vertex_dict[vertex].y - 25, vertex_dict[vertex].y + 25):
                vertex_dict[vertex].draw_vertex(1, 0, 0, 10)

                # record the vertex object in starter
                starter = vertex_dict[vertex]

                # record the coordinates of the vertex
                starter_x, starter_y = vertex_dict[vertex].x, vertex_dict[vertex].y

                # print the starter vertex and its coordinates
                print("STARTER VERTEX: " + vertex + " COORDINATES: " + str(starter_x) + "," + str(starter_y))

        starter_set = True  # the starter has been selected, so set this to true


def set_goal():
    global goal_x, goal_y, goal_set, goal
    # if starter is selected, but the goal is not selected and the mouse is released, continue
    if starter_set is True and isClicked is False and goal_set is False:
        for vertex in vertex_dict:

            # prevents starter from being selected as the goal
            if x in range(starter_x - 7, starter_x + 7) and y in range(starter_y - 50, starter_y + 50):
                return

            # if the mouse is hovering near a vertex, draw the vertex in red
            elif x in range(vertex_dict[vertex].x - 7, vertex_dict[vertex].x + 7) and y in range(
                    vertex_dict[vertex].y - 25, vertex_dict[vertex].y + 25):
                vertex_dict[vertex].draw_vertex(1, 0, 0, 10)

                # record the vertex object in goal
                goal = vertex_dict[vertex]

                # record the coordinates of the vertex
                goal_x, goal_y = vertex_dict[vertex].x, vertex_dict[vertex].y

                # print the goal and its coordinates
                print("GOAL VERTEX: " + vertex + " COORDINATES: " + str(goal_x) + "," + str(goal_y))

                goal_set = True  # set true if the goal has been selected,

        return


# record mouse move
def move(mx, my):
    global x, y
    x = mx
    y = my


# main draw function
def main():
    # global variables
    global map_draw, vertices_draw, edges_draw, bfs, starter_set, goal_set

    # Draw map if it is not drawn
    if map_draw is False:
        img = load_image("dartmouth_map.png")
        draw_image(img, 0, 0)
        map_draw = True

    # Draw vertices if they are not drawn
    if vertices_draw is False:
        draw_vertices()
        vertices_draw = True

    # Draw edges if they are not drawn
    if edges_draw is False:
        draw_edges()
        edges_draw = True

    # get the starting and goal vertices
    set_starter()
    set_goal()

    # if the start and goal are selected, and the bfs has not yet been called, continue
    if goal_set and starter_set and bfs is False:
        # grab path from the bfs function
        path = run_bfs(starter, goal)
        # bfs is now true
        bfs = True
        starter_set = True
        goal_set = True

        # draws the edges for the vertices in path
        for i in range(len(path) - 1):
            path[i].draw_edge(path[i + 1], 1, 0, 0)

# if the bfs has been run, reset the bfs along with the starter/goal points
    if bfs and starter_set and goal_set:
        bfs = False
        starter_set = False
        goal_set = False


start_graphics(main, 4000, width=FRAME_WIDTH, height=FRAME_HEIGHT, mouse_press=mousedown, mouse_release=mouseup,
               mouse_move=move)