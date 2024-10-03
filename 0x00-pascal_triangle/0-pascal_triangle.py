#!/usr/bin/python3
'''A module containing the Pascal's triangle function.
'''


def pascal_triangle(n):
    '''Create a Pascal's triangle with `n`
    representing the number of rows.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle