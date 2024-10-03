#!/usr/bin/python3
'''A module containing pascal triangle function
'''

def pascal_triangle(n):
    '''Create a pascal triangle and n represent the number of rows'''
    triangle = []
    if n <=0:
        return triangle
    
    if n ==1:
        return [[1]]
    
    if n ==2:
        return [[1], [1, 1]]
    
    triangle = [[1], [1, 1]]
    
    for i in range(2, n):
        triangle.append([1])
        for j in range(i - 1):
            triangle[i].append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        triangle[i].append(1)

    return(triangle)

    