import re

'''
    This file contains the template for Assignment3. For testing it, I will place it
    in a different directory, call the function <minimum_cost_connecting_edges>, and check its output.
    So, you can add/remove whatever you want to/from this file. But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''


def create_matrix(input_file_path):
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            l = re.findall(r'\b\d+\b', line)
            break
    points = []
    count = 0
    half = int(len(l) / 2)
    for i in range(0, half):
        points.append((l[count], l[count + 1]))
        count += 2
    matrix = []
    for i in range(0, len(points)):
        new = []
        for j in range(0, len(points)):
            dif = abs(int(points[i][0]) - int(points[j][0])) + abs(int(points[i][1]) - int(points[j][1]))
            new.append(dif)
        matrix.append(new)
    return matrix


def grab_pre_selected_edges(input_file_path):
    with open(input_file_path, "r") as input_file:
        i = 0
        for line in input_file:
            if i == 1:
                l = re.findall(r'\b\d+\b', line)
            else:
                i += 1
    edges = []
    count = 0
    for i in range(0, int(len(l) / 2)):
        edges.append((l[count], l[count + 1]))
        count += 2
    return edges


def set_pre_determined_edges_to_zero(matrix, edges):
    for (source, destination) in edges:
        matrix[int(source) - 1][int(destination) - 1] = 0
        matrix[int(destination) - 1][int(source) - 1] = 0
    return matrix


def list_edges(matrix):
    edges = []
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            src = i
            dest = j
            weight = matrix[i][j]
            if src != dest:
                edges.append((weight, src, dest))
    return edges


def partition(edges, start, end):
    """Partition the edges based on weight"""
    (pivot, _, _) = edges[start]
    low = start + 1
    high = end

    while True:
        (val, _, _) = edges[high]
        while low <= high and val >= pivot:
            high = high - 1
            if low <= high:
                (val, _, _) = edges[high]

        (val, _, _) = edges[low]
        while low <= high and val <= pivot:
            low = low + 1
            if low <= high:
                (val, _, _) = edges[low]

        if low <= high:
            edges[low], edges[high] = edges[high], edges[low]
        else:
            break
    edges[start], edges[high] = edges[high], edges[start]
    return high


def sort_edges(edges_list, start, end):
    """Partition sort the edges"""
    if start >= end:
        return
    p = partition(edges_list, start, end)
    sort_edges(edges_list, start, p - 1)
    sort_edges(edges_list, p + 1, end)


def find_root(parent, i):
    """Finds the root of a tree given the index"""
    if parent[i] == i:
        return i
    return find_root(parent, parent[i])


def join_two_trees(parent, rank, x, y):
    """Joins two trees via ranking"""
    x_root = find_root(parent, x)
    y_root = find_root(parent, y)
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


def kruskal(graph, num_vertices):
    result = []
    i, e = 0, 0
    parent = []
    rank = []
    total = 0
    for node in range(num_vertices):  # create unconnected graph
        parent.append(node)
        rank.append(0)
    while e < num_vertices - 1:  # for each edge, add to MST if doesn't create cycle
        (edge_weight, first, second) = graph[i]
        i = i + 1
        first_parent = find_root(parent, first)
        second_parent = find_root(parent, second)
        if first_parent != second_parent:  # if have same parent, then same tree, so don't add
            result.append([edge_weight, first, second])  # add edge to result
            join_two_trees(parent, rank, first_parent, second_parent)  # join the two trees together
            e = e + 1
    for weight, first, second in result:
        total += weight
    return total


def minimum_cost_connecting_edges(input_file_path, output_file_path):
    # take in matrix from file and input any predetermined edges
    matrix = create_matrix(input_file_path)
    pre_selected_edges = grab_pre_selected_edges(input_file_path)
    matrix = set_pre_determined_edges_to_zero(matrix, pre_selected_edges)

    edges_list = list_edges(matrix)
    sort_edges(edges_list, 0, len(edges_list) - 1)  # sort edges
    weight = kruskal(edges_list, len(matrix))  # run kruskal's algorithm

    # Write out to file
    out = open(output_file_path, "w")
    out.write(str(weight))
    out.close()


'''
    To test your function, you can uncomment the following command with the input/output
    files paths that you want to read from/write to.
'''

# minimum_cost_connecting_edges('input16.in', 'output.txt')
