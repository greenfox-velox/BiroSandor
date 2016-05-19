# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student():

    def __init__(self):
        self.gradelist=[]
    def add_grade(self, grade):
        if grade > 0 and grade < 6:
            self.gradelist.append(grade)

    def get_average(self):
        total = 0
        for i in self.gradelist:
            total += i
        average = total / len(self.gradelist)
        return average

student1 = Student()
student1.add_grade(1)
student1.add_grade(2)
student1.add_grade(3)
student1.add_grade(4)
student1.add_grade(5)

print (student1.get_average())
