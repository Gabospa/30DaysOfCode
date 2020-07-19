"""
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective 
phone numbers. You will then be given an unknown number of names to query your phone book for.
 For each name queried, print the associated entry from your phone book on a new line in the form 
 name=phoneNumber; if an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""

if __name__ == '__main__':
    size = int(input())
    dictionary = {}
    arr = [0]* size
    for i in range(size):
        arr[i] = list(input().split())
        dictionary[arr[i][0]] = arr[i][1]
    
    while True:
        try:
            query = input()
            if query in dictionary:
                print(f'{query}={dictionary[query]}')
            else:
                print('Not found')
        except:
            break        