# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person():

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        if birth_date < 0 or birth_date > 2016:
            raise ValueError('ERROR!!')


first = Person('Sanyi', 1988)
second = Person('Bela', 2018)




# try:
#     first = Person('Sanyi', 1988)
#     second = Person('Bela', 2018)
# except ValueError as e:
#     print(e)
