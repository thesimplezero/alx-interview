#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Parameters:
    - n (int): The number of rows for Pascal's triangle.

    Returns:
    - list of lists: A list of lists representing Pascal's triangle.
      Each inner list corresponds to a row in the triangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [a + b for a, b in zip(prev_row, prev_row[1:])] + [1]
        triangle.append(new_row)

    return triangle
