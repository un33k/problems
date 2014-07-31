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

    def calculate(matrix, matrix_h, matrix_w, next_h, next_w, last_value=0):
        """
        Local calculation recursive function.
        """

        # Stop condition 1
        if matrix[next_h][next_w] == 0:
            return last_value

        # Stop condition 2
        if next_h == matrix_h  and next_w == matrix_w:
            return last_value + 1

        # Move right
        if next_w < matrix_w:
            last_value = calculate(matrix, matrix_h, matrix_w,
              next_h, next_w + 1, last_value)

        # Move down
        if next_h < matrix_h:
            last_value = calculate(matrix, matrix_h, matrix_w,
              next_h + 1, next_w, last_value)

        # Final Result
        return last_value

    count = calculate(nXm_matrix, hight-1, width-1, 0, 0)
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
