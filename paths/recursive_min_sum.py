
import sys
import cProfile


def minSumPaths(nXm_matrix):
    """
    Returns the `minimal` path `sum` from the top left to the bottom
    right by moving right and down in a 2D array of size n x m.
    """
    hight = len(nXm_matrix)
    width = len(nXm_matrix[0])

    def calculate(matrix, matrix_h, matrix_w, next_h, next_w, last_value=0):
        """
        Local calculation recursive function.
        """
        last_value += matrix[next_h][next_w]
        if next_h == matrix_h  and next_w == matrix_w:
            return last_value

        move_right = sys.maxint
        if next_w < matrix_w:
            move_right = calculate(matrix, matrix_h, matrix_w,
              next_h, next_w + 1, last_value)

        move_down = sys.maxint
        if next_h < matrix_h:
            move_down = calculate(matrix, matrix_h, matrix_w,
              next_h + 1, next_w, last_value)

        return min(move_right, move_down)

    count = calculate(nXm_matrix, hight-1, width-1, 0, 0)
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

    count = minSumPaths(d2_matrix)
    print "---------------------"
    print "Minimum Path Sum = {}\n".format(count)


if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('run_test()')
