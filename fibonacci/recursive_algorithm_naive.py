import cProfile

def fibonacci(n):
    """
    Returns the next Fibonacci sequence for a given `n`.
    """
    if n <= 2:
        f = 1
    else:
        f = fibonacci(n - 1) + fibonacci(n - 2)
    return f


def run_test():
    """
    Test function.
    """
    for n in range(30):
        print fibonacci(n)


if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('run_test()')
