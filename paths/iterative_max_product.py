
import sys
import cProfile


def maxProductPaths(nXm_matrix):
    """
    Returns the `maximum` path `product` from the top left to the bottom
    right by moving right and down in a 2D array of size n x m.
    """
    hight = len(nXm_matrix)
    width = len(nXm_matrix[0])
    noop = 1
    grid = {}

    # create a grid system dictionary using key format of (h,w)
    for h in range(hight):
        for w in range(width):
            grid[(h, w)] = nXm_matrix[h][w]

    # start from bottom-right and move your way up
    for h in reversed(range(hight)):
        for w in reversed(range(width)):
            bottom = grid.get((h + 1, w), noop)
            right = grid.get((h, w + 1), noop)
            if not all(x == noop for x in (bottom, right)):
                grid[(h, w)] *= max(bottom, right)

    # print a matrix where (0,0) has the total max `product` number
    for h in range(hight):
        row = [str(grid[(h,w)]).rjust(5) for w in range(width)]
        print '[{}]'.format(','.join(row))

    # to traverse the the minimal product path, start from (0,0) and
    # work your way down. (take-home exercise)

    count = grid[(0,0)]
    return count


def run_test():
    """
    Test function.
    """
    d2_matrix = [
        [1,6,1],
        [3,7,2],
        [5,0,8],
        [1,6,1],
    ]

    count = maxProductPaths(d2_matrix)
    print "---------------------"
    print "Maximum Path Product = {}\n".format(count)


if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('run_test()')
