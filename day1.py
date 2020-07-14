""" Task
Complete the code in the editor below. The variables i,d, and s are already declared and initialized for you. You must:
1. Declare  variables: one of type int, one of type double, and one of type String.
2. Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
3. Use the  operator to perform the following operations:
    a. Print the sum of  plus your int variable on a new line.
    b. Print the sum of  plus your double variable to a scale of one decimal place on a new line.
    c. Concatenate  with the string you read as input and print the result on a new line.
Note: If you are using a language that doesn't support using  for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. 
The string provided in your editor must be printed first, immediately followed by the string you read as input.
"""
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
new_i = 0
new_d = 0
new = '' 
# Read and save an integer, double, and String to your variables.
new_i = int(input())
new_d = float(input())
new = input() 
# Print the sum of both integer variables on a new line.
print (i + new_i)
# Print the sum of the double variables on a new line.
print (d + new_d)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print (s + new)
