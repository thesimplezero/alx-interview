#!/usr/bin/python3
"""This module reads stdin and computes metrics"""
import sys


def print_stats(total_size, status_counts):
    """Print accumulated metrics.

    Args:
        total_size (int): The accumulated read file size.
        status_counts (dict): The accumulated count of status codes.
    """
    print(f"File size: {total_size}")

    for key in sorted(status_counts):
        print(f"{key}: {status_counts[key]}")


def process_line(line, total_size, status_counts, valid_status_codes, count):
    """Process a line and update total_size and status_counts."""
    line = line.split()

    try:
        total_size += int(line[-1])
    except (IndexError, ValueError):
        pass

    try:
        if line[-2] in valid_status_codes:
            status_counts[line[-2]] = status_counts.get(line[-2], 0) + 1
    except IndexError:
        pass

    return total_size, status_counts, count


def main():
    total_size = 0
    status_counts = {}
    valid_status_codes = {
        '200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        # Looping through each line in stdin
        for line in sys.stdin:
            count += 1

            if count == 10:
                total_size, status_counts, count = process_line(
                    line, total_size, status_counts, valid_status_codes, count
                )
                print_stats(total_size, status_counts)
                count = 0
            else:
                total_size, status_counts, count = process_line(
                    line, total_size, status_counts, valid_status_codes, count
                )

        print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interrupt by printing final accumulated metrics
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
