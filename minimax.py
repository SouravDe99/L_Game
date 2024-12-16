import csv
import sys

sys.setrecursionlimit(20000)

edges = []
explored_red = {}
explored_blue = {}


def minimax(index, depth, player):
    global counter
    print(depth)

    # base_case

    if player == 'r':
        if index in explored_blue.keys():
            if explored_blue[index] is None:
                explored_blue[index] = 0
        else:
            if vertex_degrees[index]['out_degree_red'] == 0:
                explored_blue[index] = -1
            else:
                explored_blue[index] = None
        if explored_blue[index] is not None:
            return explored_blue[index]
    if player == 'b':
        if index in explored_red.keys():
            if explored_red[index] is None:
                explored_red[index] = 0
        else:
            if vertex_degrees[index]['out_degree_blue'] == 0:
                explored_red[index] = 1
            else:
                explored_red[index] = None
        if explored_red[index] is not None:
            return explored_red[index]

    # recursive case

    if player == 'r':
        max_value = -1
        for next_index in range(0, len(edges)):
            if 'r' in edges[index][next_index]:
                value = minimax(next_index, depth + 1, 'b')
                max_value = max(max_value, value)
        if explored_blue[index] is not None and explored_blue[index] != max_value:
            counter += 1
        explored_blue[index] = max_value
        return max_value

    if player == 'b':
        min_value = 1
        for next_index in range(0, len(edges)):
            if 'b' in edges[index][next_index]:
                value = minimax(next_index, depth + 1, 'r')
                min_value = min(min_value, value)
        if explored_red[index] is not None and explored_red[index] != min_value:
            counter += 1
        explored_red[index] = min_value
        return min_value


# main

file = open("edges_restricted.csv", "r")
reader = csv.reader(file)
for row in reader:
    edges.append(row)
file.close()

file = open("vertex_degrees_restricted.txt", "r")
vertex_degrees = eval(file.read())
file.close()

counter = 0
print("Value: ", minimax(1686, 0, 'r'))
print("Number of disagreements: ", counter)