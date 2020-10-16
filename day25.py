""" 
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
Given a number, n , determine and print whether it's Prime or Not prime.

Note: If possible, try to come up with a O(n**0.5) primality algorithm, 
or see what sort of optimizations you come up with for an O(n) algorithm. 
Be sure to check out the Editorial after submitting your code!
"""

def test_prime(number):
    prime = True
    sqrt = round(number ** 0.5)
    if number == 1:
        print('Not prime')
    else:
        for i in range(2,sqrt+1):
            if number % i == 0:
                prime = False 
                break
        if prime == True:
            print('Prime')
        else:
            print('Not prime')
         
    

if __name__ == '__main__':
    size = int(input())
    for _ in range(size):
        number = int(input())
        test_prime(number)
