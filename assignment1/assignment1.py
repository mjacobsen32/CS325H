"""
    This file contains the template for Assignment1.  For testing it, I will place it
    in a different directory, call the function <count_crossing>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
"""


def array_input(input_file_path, line_num):
    with open(input_file_path, "r") as input_file:
        i = 0
        for line in input_file:
            arr = line.strip().split(",")
            if line_num == 1:
                return arr
            else:
                if i == 1:
                    return arr
            i += 1


def count_crossings(input_file_path, output_file_path):
    """
        This function will contain your code.  It wil read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.
    """
    line1 = array_input(input_file_path, 1)  # first line of input into line1
    line2 = array_input(input_file_path, 2)  # second line of input into line2

    pass


'''
    To test your function, you can uncomment the following command with the the input/output
    files paths that you want to read from/write to.
'''
sample1 = 'test_input/sample1.txt'
sample2 = 'test_input/sample2.txt'
sample3 = 'test_input/sample3.txt'

output = 'output/output1.txt'

count_crossings(sample1, output)

''' basic math behind an intersection:

line = [pi,qi]

check_intersect(line1, line2)
    if (p1 < p2):
        if (q1 >= q2): intersection
        else: no intersection
    elif (p1 > p2):
        if (q1 <= q2): intersection
        else: no intersection
    else: intersection (same p1)
    

    RECURSION IDEAS:

    [1,2,3]
    [3,2,1]

    line 1: [1,3]
    line 2: [2,2]
    line 3: [3,1]

    Now we have 3 elements:
    l1,l2,l3
    line_list = [l1,l2,l3]

    check_intersect(line_list[0],line_list[1])
    check_intersect(line_list[0],line_list[2])
    check_intersect(line_list[1],line_list[2])

    sum return values of all calls of check_intersect

'''
