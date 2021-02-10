"""
    This file contains the template for Assignment2.  For testing it, I will place it
    in a different directory, call the function <my_points_against_elmo>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
"""


# Reads a certain line from the input file
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


def my_points_against_elmo(input_file_path, output_file_path):
    """
        This function will contain your code.  It wil read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.
    """
    card_array = array_input(input_file_path, 1)
    
    total = 0
    for i in range(0, len(card_array)):
        total = total + card_array[i]
    points = total - calculate_points(card_array)

    with open(output_file_path, "w") as out:
        out.write(str(int(points)))


def calculate_points(card_array):
    """
        This is where all the calculation logic should occur
    """

    if(len(card_array) == 1):
        return(card_array[0])
    elif(len(card_array) == 2):
        return(max(card_array[0],card_array[1]))
    else:
        l = card_array[0]
        r = card_array[len(card_array)-1]
        return(max((l + min(calculate_points(card_array[2:]), calculate_points(card_array[1:-1]))),(r + min(calculate_points(card_array[:-2]), calculate_points(card_array[1:-1])))))
    return 0  # TODO set up tests to make sure file io is working as expected


if __name__ == '__main__':
    print(calculate_points([1, 2, 3]))  # should be 2
    print(calculate_points([5, 10, 2, 3]))  # should be 7
    print(calculate_points([100]))  # should be 0
