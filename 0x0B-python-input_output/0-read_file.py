#!/usr/bin/python3
"""This module contains the read_file function"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        files = file.read()
        print(files, end="")
