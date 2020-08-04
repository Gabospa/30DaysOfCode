"""
Complete the Difference class by writing the following:

- A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
- A computeDifference method that finds the maximum absolute difference between any  numbers in  and stores it in the  instance variable.

"""

class Difference:
    def __init__(self, a):
        self.__elements = a
        
	# Two loop cycles that check abs diference between elements and keep the max
    def computeDifference(self):
        max_value = 0
        for i in range(len(self.__elements)):
            for j in range(i+1, len(self.__elements)):
                result = abs(self.__elements[i]-self.__elements[j])
                if result > max_value:
                    max_value = result
        self.maximumDifference = max_value


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)