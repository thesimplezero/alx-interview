#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if given data set represents valid UTF-8 encoding
    """
    bytes_remaining = 0

    for num in data:
        if bytes_remaining:
            if not (num >> 6 == 0b10):
                return False
            bytes_remaining -= 1
        else:
            if num >> 3 == 0b11110:
                bytes_remaining = 3
            elif num >> 4 == 0b1110:
                bytes_remaining = 2
            elif num >> 5 == 0b110:
                bytes_remaining = 1
            elif num >> 7:
                return False

    return bytes_remaining == 0
