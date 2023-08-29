#!/usr/bin/python3
"""Island_Perimeter_Problem
"""


def island_perimeter(grid):
    """
    Calculates_the_perimeter_of_the_island_described_in_grid
    Args:
        grid:_2d_list_of_integers_containing_0(water)_or_1(land)
    Return:
        the_perimeter_of_the_island
    """

    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    p += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    p += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    p += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    p += 1
    return p
