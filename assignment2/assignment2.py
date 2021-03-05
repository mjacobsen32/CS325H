"""
    Code for CS325H, group assignment 2
    by Matthew Jacobsen, Ethan Hampton, & Scot Rein
    it recurses over all possible moves before selecting the best one
    based on the fact that the other player will also select the best move.
    There is some memoization optimization to reduce runtime
"""
mem_array = [[1,2,3],[2,2],[33,3]]

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


# we use a dictionary for memoization because it let's us store
# the array then the value that array returns for our function.
# we convert the array to a string, then hash the string which
# produces 64 bit numbers such that they will match if the
# arrays are the same. At this scale we don't need to worry about collisions
memoization = dict()


def my_points_against_elmo(input_file_path, output_file_path):
    # read card array in from file (on file line 1)
    card_array = array_input(input_file_path, 1)

    # make sure all items in array are integers
    card_array = list(map(int, card_array))

    # find the total sum of all cards
    total = sum(card_array)

    # we calculate elmos points/the player who goes first,
    # so figure out the second players points
    points = total - calculate_points(card_array)

    # write out to file
    with open(output_file_path, "w") as out:
        out.write(str(int(points)))

def array_in_memory(array):
    for i in range(0, len(mem_array)):
        if array == mem_array[i]:
            return(True)
    return(False)

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

    # calculate if we take the left card or right card, and if the other player
    # takes the right or left card of that
    value = (max((left + min(calculate_points(card_array[2:]), one_off_each_side)),
                 (right + min(calculate_points(card_array[:-2]), one_off_each_side))))

    # remember output for this specific array
    memoization.update({hashed_array: value})
    return value


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

print(array_in_memory([1,2,3]))
print(array_in_memory([33,3]))
print(array_in_memory([3,33]))
