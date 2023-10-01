#!/usr/bin/python3
"""
Module to compute the perimeter of an island in a grid

The grid is represented as a list of lists of integers where:
    0 represents water
    1 represents land

This module contains a function island_perimeter that returns the perimeter.
"""


def island_perimeter(grid):
    """
    Return the perimeter of the island described in grid.

    Args:
    - grid (list of lists of int): Representation of the island.

    Returns:
    - int: Perimeter of the island.
    """

    # Initialize the perimeter to 0
    perimeter = 0

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):

            # If the cell is land
            if grid[i][j] == 1:

                # Check for all directions around the cell

                # Above
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1

                # Below
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1

                # Left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1

                # Right
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
