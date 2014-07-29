import cProfile


def numberOfPaths(nXm_matrix):
    """
    Returns the total number of paths from the top left
    to the bottom right by moving right and down in a 2D array
    of size n x m. Where cells can only contain `1` or `0` while
    real paths can only contain `1`.
    """
    hight = len(nXm_matrix)
    width = len(nXm_matrix[0])
    grid = {}

    # create a grid system dictionary using key format of (h,w)
    for h in range(hight):
        for w in range(width):
            grid[(h, w)] = nXm_matrix[h][w]

    # start from top-left and move your way down
    for h in range(hight):
        for w in range(width):
            if (h,w) != (0,0) and grid[(h, w)]:
                top = (h - 1, w)
                left = (h, w - 1)
                grid[(h, w)] = grid.get(top, 0) + grid.get(left, 0)

    # print a matrix where the total number of paths from the top-left
    # to each cell is stored in the cell itself.
    for h in range(hight):
        row = [str(grid[(h,w)]).rjust(5) for w in range(width)]
        print '[{}]'.format(','.join(row))

    count = grid[(hight-1, width-1)]
    return count

def run_test():
    """
    Test function.
    """
    d2_matrix = [
        [1,1,1,1,1,1],
        [1,1,0,1,1,1],
        [1,1,1,0,1,1],
        [1,1,0,1,1,1],
        [1,1,1,1,0,1],
    ]

    count = numberOfPaths(d2_matrix)
    print "---------------------"
    print "Total Number of Paths = {}\n".format(count)


if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('run_test()')
