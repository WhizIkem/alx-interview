from collections import defaultdict
import signal
import sys

# Dictionary to store status codes and their counts
status_code_counts = defaultdict(int)

# Total file size
total_size = 0

# Function to print statistics
def print_statistics(signum, frame):
    print(f"Total file size: File size: {total_size}")
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(f"{status_code}: {count}")

# Register the signal handler
signal.signal(signal.SIGINT, print_statistics)

# Read input line by line
for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) == 10 and parts[5] == '"GET' and parts[9] == "HTTP/1.1\"":
        ip_address, status_code, file_size = parts[0], parts[8], int(parts[6])
        if status_code.isdigit():
            status_code_counts[status_code] += 1
        total_size += file_size

        # Print statistics every 10 lines
        if total_size % 10 == 0:
            print_statistics(None, None)