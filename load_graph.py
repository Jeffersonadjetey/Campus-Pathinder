# Name - Jefferson Adjetey
# Date - March 12, 2021
# Purpose - Create a graph of vertices with the use of a dictionary

from vertex import Vertex

v_dict = {}


def load_graph(file):  # function to load the vertices

    fp = open(file, "r")  # open the given file for reading

    for l in fp:
        w_l = l.strip().split(";")  # splits the line into three sections
        w_l[0] = w_l[0].strip()  # strip the whitespace from the name section of the line

        x_y = w_l[2]  # store the coordinates from the second section of the line
        x_y_values = x_y.split(",")  # split the coordinates so they can be accessed
        # individually

        v = Vertex(w_l[0])  # create a vertex object
        v.x = int(x_y_values[0])  # assign the coordinates to the instance variables of the object
        v.y = int(x_y_values[1])

        v_dict[w_l[0]] = v  # add the name to the dictionary with the object as the value

    fp.close()  # close file for reading

    fp = open(file, "r")

    for l in fp:
        # split each line into three sections and remove whitespace
        w_l = l.strip().split(";")
        w_l[0] = w_l[0].strip()

        # split the adjacent vertices up so they can be individually accessed
        adjacents = w_l[1]
        adj_list = adjacents.split(",")

        # access the vertex object of the line
        v = v_dict[w_l[0]]

        for adj in adj_list:
            adj = adj.strip()  # strips whitespace
            adj_v = v_dict[adj]  # accesses the adjacent vertex object using its name
            v.adj.append(adj_v)  # append the adjacent vertex object to the vertex's adjacent list

    fp.close()  # close file for reading
    return v_dict  # return complete dictionary


load_graph("dartmouth_graph.txt")