"""
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer 
denoting the maximum number of consecutive 1's in 's binary representation.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#fuction to pass to binary
def binary(n):
    cont = ''
    while n >= 0:
        if n <= 1:
            cont = str(n)+cont
            break
        res = n % 2
        cont = str(res)+ cont    
        n = n // 2
    return cont


#fuction to count the maximum number of consecutive 1's 
def one_count(string):
    cont = 1
    max_cont = 0
    size = len(string)
    for i in range(size-1):
        if string[i] == '1' and string[i+1]=='1':
            cont += 1
            if cont > max_cont:
                max_cont = cont
        else:
            cont = 1
    if cont > max_cont:
        max_cont = 1
    return max_cont

if __name__ == '__main__':
    n = int(input())
    print (one_count(binary(n)))