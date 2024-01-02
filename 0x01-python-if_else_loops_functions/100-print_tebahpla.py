#!/usr/bin/python3
for a in reversed(range(97, 123)):
    result = f"{chr(a if (a % 2 == 0) else (a - 32))}"
    print(result, end='')

print()

