#!/usr/bin/python3
'''caluculate the minimum number of operation to copy h.
'''

def minOperations(n):
    if n < 2:
        return 0

    operations = 0
    i = 2

    while i <= n: #2 is less than 10 #i =3 less than 10
        while n % i == 0: #10%2 =0
            operations += i # operations = 2
            n //= i #n = 10//2 = 5
        i += 1 #i = 3

    return operations
