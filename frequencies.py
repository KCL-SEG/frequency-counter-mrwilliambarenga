"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for item in items:
        item_string = str(item)
        if item_string not in frequencies:
            frequencies[item_string] = 1
        else:
            frequencies[item_string] += 1

    return frequencies