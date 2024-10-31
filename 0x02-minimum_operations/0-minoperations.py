#!/usr/bin/python3
'''caluculate the minimum number of operation to copy h.
'''

def minOperations(n):
    if n < 2:
        return 0

    operations = 0
    i = 2

    while i <= n:
        while n % i == 0:
            operations += i
            n //= i
        i += 1

    return operations
