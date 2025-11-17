#!/usr/bin/env python3
from argparse import ArgumentParser
"""Computation of weighted average of squares."""


def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares) / len(list_of_numbers)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]

    """
    # all_numbers = []
    # for s in list_of_strings:
    #     # Take each string in the list, split it into substrings separated by
    #     # whitespace, and collect them into a single list...
    all_numbers = [int(token) 
                   for s in list_of_strings  
                   for token in s.split()]     
    
    return all_numbers[:len(list_of_strings)]

def read_numbers_from_file(filename):
    """Read numbers from a file and return as a list of floats
    
    The file should contain numbers separated by spaces or newlines.
    """
    with open(filename, 'r') as f:
        content = f.read()
        # Split by whitespace (spaces, tabs, newlines)
        number_strings = content.split()
        return convert_numbers(number_strings)

def process():
    parser = ArgumentParser(description="Average of squares")
    
    # Positional argument for numbers file
    parser.add_argument('file_numbers', 
                        help="Text file containing list of numbers")
    
    # Optional argument for weights file
    parser.add_argument('-w', '--weights', 
                        help="Text file containing list of weights (optional)")
    
    arguments = parser.parse_args()
    
    # Read numbers from file
    numbers = read_numbers_from_file(arguments.file_numbers)
    
    # Read weights from file if provided
    weights = read_numbers_from_file(arguments.weights) if arguments.weights else None
    
    result = average_of_squares(numbers, weights)
    print(result)

if __name__ == "__main__":
    process()