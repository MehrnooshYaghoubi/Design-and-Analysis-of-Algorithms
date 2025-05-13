"""
This is a pure python implementation of the shell sort algorithm

For doctests run following command:
python -m doctest -v shell_sort.py
or
python3 -m doctest -v shell_sort.py

For manual testing run:
python shell_sort.py
"""
from __future__ import print_function


def shell_sort(collection):

    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(collection):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
            i += 1

    return collection

if __name__ == '__main__':

    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(shell_sort(unsorted))
