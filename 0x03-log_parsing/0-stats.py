#!/usr/bin/env python3

import sys

TOTAL_LINES_TO_READ = 10

# Status codes to track
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Dictionary to store the number of lines by status code
num_lines_by_status = {}
for code in status_codes:
    num_lines_by_status[code] = 0

# Total file size
total_size = 0

# Counter to keep track of the number of lines read
line_count = 0

try:
    for line in sys.stdin:
        # Parse the line
        try:
            parts = line.split()
            ip_address = parts[0]
            date = parts[3][1:]
            status_code = int(parts[8])
            file_size = int(parts[9])
        except:
            # Skip this line if it doesn't match the expected format
            continue

        # Update metrics
        total_size += file_size
        num_lines_by_status[status_code] += 1
        line_count += 1

        # Print stats every TOTAL_LINES_TO_READ lines
        if line_count % TOTAL_LINES_TO_READ == 0:
            print("Total file size: {}".format(total_size))
            for code in sorted(num_lines_by_status.keys()):
                if num_lines_by_status[code] > 0:
                    print("{}: {}".format(code, num_lines_by_status[code]))

except KeyboardInterrupt:
    # Print final stats on keyboard interrupt
    print("Total file size: {}".format(total_size))
    for code in sorted(num_lines_by_status.keys()):
        if num_lines_by_status[code] > 0:
            print("{}: {}".format(code, num_lines_by_status[code]))

