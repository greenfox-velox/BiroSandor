# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        greet = 'Hello'
        print (greet, self.first_name, self.last_name)

class Student(Person):

    def __init__(self):
        self.gradelist=[]

    def add_grade(self, grade):
        if self.grade > 0 and self.grade < 6:
            self.gradelist.append(self.grade)

    def get_average(self):
        total = 0
        for i in self.gradelist:
            total += i
        self.average = total / len(self.gradelist)
        return self.average

    def salute(self):
        grades = 'Your grades is:'
        avarage = 'and your average is:'
        print(self.first_name, self.last_name, grades, self.grade, average, self.average)

person1 = Person('Lechi', 'Kurbanov')
print (person1.greet())
person1.add_grade(1)
person1.add_grade(2)
person1.add_grade(3)
person1.add_grade(4)
person1.add_grade(5)

print (person1.salute())
