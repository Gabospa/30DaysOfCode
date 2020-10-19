""" 
Given set S ={1,2,3,.. ,N} . Find two integers, A and B (where A < B ), 
from set  such that the value of A&B is the maximum possible and also less 
than a given integer K. In this case, & represents the bitwise AND operator. 
""" 
#!/bin/python3

import math
import os
import random
import re
import sys
from math import log

def main(n, k):
    power = int(log(n,2))-1
    floor = 2**power
    max_result = 0
    for i in range(floor+1,n+1):
        for j in range(1,i):
            operation = i & j
            if (operation > max_result and operation < k):
                max_result = operation
            if max_result == k-1:
                break
    return max_result 
            
            
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(main(n,k))
