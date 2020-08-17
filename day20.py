"""
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort 
algorithm above. Once sorted, print the following 3 lines:

    1. Array is sorted in numSwaps swaps.
    where  is the number of swaps that took place.
    2. First Element: firstElement
    where  is the first element in the sorted array.
    3. Last Element: lastElement
    where  is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps 
that occur during execution.
"""

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
num_swaps = 0

for i in range (n):
    for j in range (i+1,len(a)):
        if a[i] > a[j]:
            a[i],a[j]= a[j],a[i]
            num_swaps += 1
    if num_swaps == 0:
        break

print(f'Array is sorted in {num_swaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[n-1]}')

            
