#!/usr/bin/python3
"""Defines a text file-Append function"""
def append_write(filename="", text=""):
     """Append the contents of a UTF8 text file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
