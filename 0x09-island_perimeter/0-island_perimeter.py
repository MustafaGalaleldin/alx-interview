#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:  # Land cell
                # Add 4 for the cell itself
                perimeter += 4

                # Subtract 1 for each neighboring land cell
                if row > 0 and grid[row - 1][col] == 1:  # Top neighbor
                    perimeter -= 1
                if row < len(grid) - 1 and grid[row + 1][col] == 1:
                    # for the Bottom neighbor
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    # for the Left neighbor
                    perimeter -= 1
                if col < len(grid[row]) - 1 and grid[row][col + 1] == 1:
                    # for the Right neighbor
                    perimeter -= 1

    return perimeter
