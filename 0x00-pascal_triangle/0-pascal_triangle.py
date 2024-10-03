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

    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    print(triangle)
    return triangle