
import sys
import cProfile


def maxSumPaths(nXm_matrix):
    """
    Returns the `maximum` path `sum` from the top left to the bottom
    right by moving right and down in a 2D array of size n x m.
    """
    hight = len(nXm_matrix)
    width = len(nXm_matrix[0])
    smallest_num = -1 * sys.maxint
    grid = {}

    # create a grid system dictionary using key format of (h,w)
    for h in range(hight):
        for w in range(width):
            grid[(h, w)] = nXm_matrix[h][w]

    # start from bottom-right and move your way up
    for h in reversed(range(hight)):
        for w in reversed(range(width)):
            bottom = grid.get((h + 1, w), smallest_num)
            right = grid.get((h, w + 1), smallest_num)
            if not all(x == smallest_num for x in (bottom, right)):
                grid[(h, w)] += max(bottom, right)

    # print a matrix where (0,0) has the total max sum
    for h in range(hight):
        row = [str(grid[(h,w)]).rjust(5) for w in range(width)]
        print '[{}]'.format(','.join(row))

    # to traverse the the minimal sum path, start from (0,0) and
    # work your way down. (take-home exercise)

    count = grid[(0,0)]
    return count


def run_test():
    """
    Test function.
    """
    d2_matrix = [
        [131, 673, 234, 103, 18],
        [201, 96,  342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37,  331],
    ]

    count = maxSumPaths(d2_matrix)
    print "---------------------"
    print "Maximum Path Sum = {}\n".format(count)


if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('run_test()')
