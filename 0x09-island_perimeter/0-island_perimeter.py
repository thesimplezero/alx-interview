#!/usr/bin/python3

"""
This script calculates the perimeter of an island represented in a 2D grid.
The island is represented by 1s and the water is represented by 0s. 
The grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island.
"""

def island_perimeter(grid):
    """
    Function to calculate the perimeter of the island in the grid.

    Parameters:
    grid (List[List[int]]): 2D list of integers where 1 represents land and 0 represents water.

    Returns:
    int: The perimeter of the island.
    """
    # Initialize perimeter to 0
    perimeter = 0

    # Iterate over each cell in the grid
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell:  # If the cell is land (1)
                perimeter += 4  # Add 4 for each land cell

                # Subtract 2 for each internal edge (shared edge between two land cells)
                if i > 0 and grid[i - 1][j]:  # Check cell above if it exists
                    perimeter -= 2
                if j > 0 and grid[i][j - 1]:  # Check cell to the left if it exists
                    perimeter -= 2

    return perimeter
