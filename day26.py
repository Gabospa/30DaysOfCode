"""
Your local library needs your help! Given the expected and actual return dates for a library book, 
create a program that calculates the fine (if any). The fee structure is as follows:

1.If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0).
2.If the book is returned after the expected return day but still within the same calendar month 
and year as the expected return date, fine=15 Hackos x (number of days late) .
3.If the book is returned after the expected return month but still within the same calendar year 
as the expected return date, the fine = 500 Hackos x (number of months late) .
4.If the book is returned after the calendar year in which it was expected, there is a fixed fine of 1000 Hackos.

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT


def check_fine(actual_date, expected_date):
    
    if actual_date[2] <= expected_date[2]:
        if actual_date[2] < expected_date[2]:
            return 0
        if actual_date[1] <= expected_date[1]:
            if actual_date[0] <= expected_date[0]:
                return 0
            else:
                return 15 * (actual_date[0] - expected_date[0])
        else:
            return 500 * (actual_date[1] - expected_date[1])
    else:
        return 10000

if __name__ == '__main__':
    actual_date = list(map(int, input().strip().split()))
    expected_date = list(map(int, input().strip().split()))
    print(check_fine(actual_date, expected_date))
    
