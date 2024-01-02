#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        num = 32 if 'a' <= char <= 'z' else 0
        result += f"{chr(ord(char) - num)}"
    print(result)
