#!/usr/bin/python3

"""
Module with a function canUnlockAll to determine if all
locked boxes can be opened.
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): List of lists representing locked boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """

    if not boxes:
        return False

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    keys_stack = [0]

    while keys_stack:
        current_box = keys_stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys_stack.append(key)

    return all(unlocked_boxes)


if __name__ == "__main__":
    test_cases = [
        [[1], [2], [3], [4], []],
        [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]],
        [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    ]

    for boxes in test_cases:
        print(canUnlockAll(boxes))
