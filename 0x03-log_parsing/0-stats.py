#!/usr/bin/python3

import sys

# Dictionary to store status code counts
status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

total_file_size = 0
line_count = 0

def print_statistics():
    print("Total file size: File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] != 0:
            print("{}: {}".format(status_code, status_code_counts[status_code]))

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        
        if len(parts) == 10 and parts[5] == '"GET' and parts[9] == "HTTP/1.1\"":
            try:
                file_size = int(parts[-1])
                status_code = parts[-2]
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                total_file_size += file_size
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics()
            except:
                pass
except KeyboardInterrupt:
    print_statistics()
