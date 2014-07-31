import os
import sys
import time
import random


class ConwaysGameOfLife(object):
    """
    An approach to the Conway's Game of Life
    http://en.wikipedia.org/wiki/Conway's_Game_of_Life

    Instruction: Open a terminal (Mac?) 170 x 40, then run this script
    and see it for yourself. It is fun."""

    HEIGHT = 40
    WIDTH = 80
    DEAD, ALIVE = range(2)

    def __init__(self, height=40, width=80):
        self.HEIGHT = height
        self.WIDTH = width

    def get_grid(self, seed=False):
        grid = {}
        for i in range(self.WIDTH):
            for n in range(self.HEIGHT):
                grid[(i, n)] = self.DEAD

        if seed:
            seeded_cell = (
                random.choice(range(self.WIDTH)),
                random.choice(range(self.HEIGHT))
            )
            neighbours = self.get_neighbours(seeded_cell)
            for a in range(3):
                i = random.choice(range(len(neighbours)))
                while grid[neighbours[i]] == self.ALIVE:
                    i = random.choice(range(len(neighbours)))
                grid[neighbours[i]] = self.ALIVE

        return grid

    def get_neighbours(self, cell):
        x, y = cell
        possible_neighbours = [
            (x-1, y-1),
            (x, y-1),
            (x+1, y-1),
            (x+1, y),
            (x+1, y+1),
            (x, y+1),
            (x-1, y+1),
            (x-1, y)
        ]
        real_neighbours = []
        for n in possible_neighbours:
            if n[0] >= 0 and n[0] < self.WIDTH:
                if n[1] >= 0 and n[1] < self.HEIGHT:
                    real_neighbours.append(n)
        return real_neighbours


    def get_neighbours_total_living(self, grid, cell):
        neighbours = self.get_neighbours(cell)
        total = 0
        for n in neighbours:
            if grid[n] == 1:
                total += 1
        return total

    def tick(self, grid):

        new_grid = self.get_grid()

        for i in range(self.WIDTH):
            for n in range(self.HEIGHT):
                living_neighbours = self.get_neighbours_total_living(grid, (i, n))
                if living_neighbours == 2 or living_neighbours == 3:
                    new_grid[(i,n)] = self.ALIVE
                elif grid[(i,n)] == self.DEAD and living_neighbours == 3:
                    new_grid[(i,n)] = self.ALIVE

        return new_grid

    def print_grid(self, grid):
        line = ''
        for i in range(self.HEIGHT):
            line += '|'
            for n in range(self.WIDTH):
                line += '*|' if grid[(n, i)] == 1 else ' |'
            line += '\n'
        sys.stderr.write (line)

    def run(self, sleep=1):
        grid = self.get_grid(seed=True)
        self.print_grid(grid)

        while True:
            grid = self.tick(grid)
            self.print_grid(grid)
            time.sleep(sleep)


def run_test():
    """
    Test function.
    """
    conway = ConwaysGameOfLife()
    conway.run()


if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    run_test()
