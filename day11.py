"""
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum

"""

#!/bin/python3

import math
import os
import random
import re
import sys

def obtain_hourglasses(arr: list):
    #start an matrix of 0's
    hour_arr = [[0 for i in range(4)] for j in range(4)]
    #find all hourglasses in a single matrix
    for j in range (4):
        for i in range(4):
            hour_arr[j][i] = [arr[0+j][0+i],arr[0+j][1+i],arr[0+j][2+i],arr[1+j][1+i],arr[2+j][0+i],arr[2+j][1+i],arr[2+j][2+i]]
    return hour_arr 

def check_max_sum(arr: list):
    # check the sum of each hourglass and return the max
    max_sum = 0
    acum = 0
    cont = 0
    for i in arr:
        for j in i:
            for k in j:
                acum += k   
            if cont == 0:
                    max_sum = acum
            cont +=1
            if acum > max_sum :
                max_sum = acum
            acum = 0
    return max_sum


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(check_max_sum(obtain_hourglasses(arr)))
