#!/usr/bin/python3

import sys

def print_stats(total_file_size, status_counts):
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        count = status_counts[code]
        if count > 0:
            print("{}: {}".format(code, count))

total_file_size = 0
status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
                 "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        if len(parts) == 10 and parts[5] == '"GET' and parts[9] == "HTTP/1.1\"":
            try:
                file_size = int(parts[-1])
                status_code = parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
                total_file_size += file_size
                line_count += 1

                if line_count == 10:
                    print_stats(total_file_size, status_counts)
                    line_count = 0
            except:
                pass
except KeyboardInterrupt:
    print_stats(total_file_size, status_counts)
