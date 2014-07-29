import cProfile

def fib(n):
    """
    Returns the next Fibonacci sequence for a given `n`.
    """
    if n <= 2:
        f = 1
    else:
        f = fib(n - 1) + fib(n - 2)
    return f


def main():
    for n in range(30):
        print fib(n)


if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('main()')
