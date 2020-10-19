"""
Consider a database table, Emails, which has the attributes First Name 
and Email ID. Given N rows of data simulating the Emails table, 
print an alphabetically-ordered list of people whose email address ends in @gmail.com.

"""
#!/bin/python3

import math
import os
import random
import re
import sys

def check_gmail(email):
    is_gmail = re.findall(r'\w+@gmail.\w+',email)
    if(is_gmail):
        return True
    else:
        return False
        
if __name__ == '__main__':
    N = int(input())
    list = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        
        if check_gmail(emailID):
            list.append(firstName)
    list.sort()
    for i in list:
        print(i)
