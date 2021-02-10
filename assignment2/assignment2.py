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


memoization = dict()


def my_points_against_elmo(input_file_path, output_file_path):
    """
        This function will contain your code.  It wil read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.
    """
    card_array = array_input(input_file_path, 1)

    # make sure all items in array are integers
    card_array = list(map(int, card_array))

    # find the total sum of all cards
    total = sum(card_array)

    # we calculate elmos points/the player who goes first,
    # so figure out the second players points
    points = total - calculate_points(card_array)

    with open(output_file_path, "w") as out:
        out.write(str(int(points)))


def calculate_points(card_array):
    """
        The recursive function
    """
    # the two base cases (which we don't bother using memoization for)
    if len(card_array) == 1:
        return card_array[0]
    elif len(card_array) == 2:
        return max(card_array[0], card_array[1])

    # convert the input to a string then turn it into a 64 bit (nearly unique) number
    hashed_array = hash(str(card_array))

    # see if we have calculated this previously
    saved_value = memoization.get(hashed_array)
    if saved_value:
        return saved_value

    left = card_array[0]
    right = card_array[len(card_array) - 1]

    # since we use this value twice, might as well only compute it once
    one_off_each_side = calculate_points(card_array[1:-1])

    value = (max((left + min(calculate_points(card_array[2:]), one_off_each_side)),
                 (right + min(calculate_points(card_array[:-2]), one_off_each_side))))

    # remember output for this specific array
    memoization.update({hashed_array: value})
    return value


if __name__ == '__main__':
    print(calculate_points([1, 2, 3]))  # should be 2
    print(calculate_points([5, 10, 2, 3]))  # should be 7
    print(calculate_points([100]))  # should be 0
    print(calculate_points([i for i in range(1000)]))
    # print(calculate_points([random.randint(0, 10000) for i in range(1000)]))
