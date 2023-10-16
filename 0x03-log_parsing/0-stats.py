#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0
batch_count = 0

try:
    for line in sys.stdin:
        try:
            ip, _, _, request, status_code, file_size = line.split()
            if request != 'GET /projects/260 HTTP/1.1':
                continue
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        status_codes[status_code] += 1
        total_file_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print(f'File size: {total_file_size}')
            for code in sorted(status_codes):
                if status_codes[code] > 0:
                    print(f'{code}: {status_codes[code]}')
            batch_count += 1
            line_count = 0

except KeyboardInterrupt:
    print(f'File size: {total_file_size}')
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f'{code}: {status_codes[code]}')
    sys.exit(0)

# Ensure the file ends with a newline character
print()