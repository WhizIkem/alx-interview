#!/usr/bin/python3
"""
script that reads stdin line by line and computes the metrics
"""
import sys
import re
import signal


def print_stats(status_codes, total_size):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    line_count = 0
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    pattern = (
        r'\d+\.\d+\.\d+\.\d+ - \[.*\] '
        r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    )

    try:
        for line in sys.stdin:
            match = re.search(pattern, line)
            if match:
                status = int(match.group(1))
                size = int(match.group(2))
                if status in status_codes:
                    status_codes[status] += 1
                total_size += size
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(status_codes, total_size)

    except KeyboardInterrupt:
        print_stats(status_codes, total_size)
        raise

    print_stats(status_codes, total_size)
