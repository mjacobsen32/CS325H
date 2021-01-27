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


def find_median(line):
    # base case, handles 5 numbers in constant time
    if len(line) <= 5:
        line.sort()
        return line[int(len(line) / 2)]

    # divide into the groups of 5 and finds median
    medians = []
    groups_index = 0
    while groups_index + 5 < len(line) - 1:
        medians.append(find_median(line[groups_index:groups_index + 5]))
        groups_index += 5

    # find median of medians
    mom = find_median(medians)
    less_than_mom = []
    greater_than_mom = []

    # partition array (into two diff arrays)
    for i in line:
        if i < mom:
            less_than_mom.append(i)
        if i > mom:
            greater_than_mom.append(i)

    # recurse or return based on where we stand
    if len(line) < len(less_than_mom):
        return find_median(less_than_mom)
    elif len(line) > len(less_than_mom) + 1:
        return find_median(greater_than_mom)
    else:
        return mom


# an overall O(3n) function, so O(n)
def find_median_index(wires):
    line = []
    for x in range(len(wires)):  # take O(n) to just grab top line
        line.append(wires[x][0])
    mid = find_median(line)  # use above function to find median value
    for i in range(len(line)):  # another O(n) to find the index again
        if line[i] == mid:
            return i


def recurse_crossing(lines):
    # base cases
    if len(lines) == 2:
        return check_intersect(lines[0], lines[1])
    if len(lines) <= 1:
        return 0

    # find median to insure correct run time
    median_index = find_median_index(lines)
    median = lines[median_index]

    intersections = 0
    left = list()
    right = list()
    for i in range(0, len(lines)):
        # ignore self check
        if i == median_index:
            continue
        # if line intersects then add it to both
        if check_intersect(median, lines[i]) == 1:
            intersections += 1
            left.append(lines[i])
            right.append(lines[i])
        else:
            # otherwise add it to just the right or left lists
            if lines[i][0] > median[0]:  # to the right
                right.append(lines[i])
            else:  # to the left
                left.append(lines[i])

    # if the right and left are the same we don't want to count them twice
    if left == right:
        left.clear()

    # recurse
    intersections += recurse_crossing(left)
    intersections += recurse_crossing(right)
    return intersections


def count_crossings(input_file_path, output_file_path):
    """
        This function will contain your code.  It wil read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.
    """
    line1 = array_input(input_file_path, 1)  # first line of input into line1
    line2 = array_input(input_file_path, 2)  # second line of input into line2

    line_list = list()
    for i in range(0, len(line1)):
        line_list.append([int(line1[i]), int(line2[i])])

    total = 0  # used to track runtime

    intersections = 0
    for i in range(0, len(line_list)):
        for j in range(i + 1, len(line_list)):
            intersections += check_intersect(line_list[i], line_list[j])
            total += 1

    with open(output_file_path, "w") as out:
        out.write(str(int(intersections)))

    print("iter:", total, " count:", len(line_list))


# Find median
# find points that intersect, add them to both left and right
# find points on left, add to left
# find points on right, add to right
# recurse until there are separation of 1 and 2 points. Check the 2 points for intersection
# check bottom of tree for intersections and count

'''
    To test your function, you can uncomment the following command with the the input/output
    files paths that you want to read from/write to.
'''
sample1 = 'test_input/sample1.txt'
sample2 = 'test_input/sample2.txt'
sample3 = 'test_input/sample3.txt'

output = 'output/output1.txt'

# count_crossings(sample1, output)
print(find_median_index([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]))
