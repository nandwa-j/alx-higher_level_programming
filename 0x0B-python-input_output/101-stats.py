#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics."""

import sys

if __name__ == "__main__":
    size = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        line_count = 0
        for line in sys.stdin:
            try:
                parts = line.split(" ")
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                size += file_size
                if status_code in codes:
                    codes[status_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print("File size: {}".format(size))
                    for code in sorted(codes.keys()):
                        if codes[code] != 0:
                            print("{}: {}".format(code, codes[code]))
            except (ValueError, IndexError):
                pass
    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for code in sorted(codes.keys()):
            if codes[code] != 0:
                print("{}: {}".format(code, codes[code]))
        raise

