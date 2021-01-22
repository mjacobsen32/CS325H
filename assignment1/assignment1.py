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


def check_intersect(line1, line2):
    p1 = line1[0]
    q1 = line1[1]
    p2 = line2[0]
    q2 = line2[1]
    if p1 < p2:
        if q1 >= q2:
            return 1
        else:
            return 0
    elif p1 > p2:
        if q1 <= q2:
            return 1
        else:
            return 0
    else:
        return 1


def count_crossings(input_file_path, output_file_path):
    """
        This function will contain your code.  It wil read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.
    """
    line1 = array_input(input_file_path, 1)  # first line of input into line1
    line2 = array_input(input_file_path, 2)  # second line of input into line2

    line_list = list()
    counter = 0  # TODO remove/replace with better name
    for p in line1:
        line_list.append([int(p), int(line2[counter])])
        counter += 1

    total = 0  # used to track runtime

    counter = 0
    for i in range(0, len(line_list)):
        for j in range(i+1, len(line_list)):
            counter += check_intersect(line_list[i], line_list[j])
            total += 1

    with open(output_file_path, "w") as out:
        out.write(str(int(counter)))

    print("iter:", total, " count:", len(line_list))


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
