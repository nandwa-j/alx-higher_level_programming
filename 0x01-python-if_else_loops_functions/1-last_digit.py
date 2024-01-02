#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last-digit = abs(number) % 10

if number < 0:
    last-digit *= -1

print(f"Last digit of {number} is ", end='')

if lastdigit == 0:
    print(f"{last-digit} and is 0")

elif lastdigit > 5:
        print(f"{last-digit} and is greater than 5")

else:
    print(f"{last-digit} and is less than 6 and not 0"))
