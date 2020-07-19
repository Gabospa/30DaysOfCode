"""
Given a string, S, of length N that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters as 2 
space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

def separate(arr):
    even = arr[::2]
    odd = arr[1::2]
    result = even + ' ' + odd
    return result

if __name__ == '__main__':
    size = int(input())
    arry = [0 for i in range(size)]
    for i in range(size):
        arry[i]= input()
        print(separate(arry[i]))
