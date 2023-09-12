#!/usr/bin/python3
"""Defines a text file-Write function"""


def write_file(filename="", text=""):
    """Write the contents of a UTF8 text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
