"""
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

1.A Student class constructor, which has  parameters:
2.A string, firstName .
3.A string, lastName.
4.An integer, id.
5.An integer array (or vector) of test scores, scores.
6.A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average: O,E,A,P,D,T

"""
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        grades = self.scores
        lenght = len(grades)
        acc = 0
        for i in grades:
            acc += i
        value = acc/lenght
        if value < 40:
            return 'T'
        elif value < 55 and value >= 40:
            return 'D'
        elif value < 70 and value >= 55:
            return 'P'
        elif value < 80 and value >= 70:
            return 'A'
        elif value < 90 and value >= 80:
            return 'E'
        elif value >= 90:
            return 'O'     

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())