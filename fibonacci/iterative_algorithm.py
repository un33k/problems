import cProfile

memorized = {}
def fib(n):
    """
    Returns the next Fibonacci sequence for a given `n`.
    """
    for k in range(1, n+1):
        if k <= 2:
            f = 1
        else:
            f = memorized[k - 1] + memorized[k - 2]
        memorized[k] = f
    return memorized[n]


def main():
    for n in range(1, 30):
        print fib(n)


if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('main()')
