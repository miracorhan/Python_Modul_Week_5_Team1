class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        # Call the constructor of the base class (Person)
        super().__init__(firstName, lastName, idNumber)
        # Initialize the scores array
        self.scores = scores
    
    def calculate(self):
        # Calculate the average score
        avg_score = sum(self.scores) / len(self.scores)
        
        # Determine the grade based on the average score
        if avg_score >= 90:
            return 'O'
        elif avg_score >= 80:
            return 'E'
        elif avg_score >= 70:
            return 'A'
        elif avg_score >= 55:
            return 'P'
        elif avg_score >= 40:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())