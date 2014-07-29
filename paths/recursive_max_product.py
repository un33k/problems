
import sys
import cProfile


def maxProductPaths(nXm_matrix):
    """
    Returns the `maximum` path `product` from the top left to the bottom
    right by moving right and down in a 2D array of size n x m.
    """
    hight = len(nXm_matrix)
    width = len(nXm_matrix[0])

    def calculate(matrix, matrix_h, matrix_w, next_h, next_w, last_value=1):
        """
        Local calculation recursive function.
        """
        last_value *= matrix[next_h][next_w]
        if next_h == matrix_h  and next_w == matrix_w:
            return last_value

        move_right = 0
        if next_w < matrix_w:
            move_right = calculate(matrix, matrix_h, matrix_w,
              next_h, next_w + 1, last_value)

        move_down = 0
        if next_h < matrix_h:
            move_down = calculate(matrix, matrix_h, matrix_w,
              next_h + 1, next_w, last_value)

        return max(move_right, move_down)

    count = calculate(nXm_matrix, hight-1, width-1, 0, 0)
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
