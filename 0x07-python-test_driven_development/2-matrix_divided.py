#!/usr/bin/python3
"""Module for divide a matrix"""


def matrix_divided(matrix, div):
    """divide a matrix of list
    Args:
        matrix (list): lst of list of intengers/floats
        div (int/float): integer or float divisor
    Raises:
        TypeError: if types don't match
        ZeroDivisionError: if divisor is 0
        TypeError: if div is not a number
    Returns:
        list: a new matrix with the result
    """
    m1 = "matrix must be a matrix (list of lists) of integers/floats"
    m2 = "Each row of the matrix must have the same size"
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError(m1)
    sizelist = len(matrix[0])
    for lst in matrix:
        if len(lst) is 0:
            raise TypeError(m1)
        if sizelist != len(lst):
            raise TypeError(m2)
        for num in lst:
            if type(num) not in (int, float) or type(lst) != list:
                raise TypeError(m1)

    result = []
    for l in matrix:
        tempList = []
        for n in l:
            tempList.append(round(n/div, 2))
        result.append(tempList)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
