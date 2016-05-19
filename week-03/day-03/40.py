students = [
    {'name': 'Rezso', 'age': 9.5, 'candies': 2},
    {'name': 'Gerzson', 'age': 10, 'candies': 1},
    {'name': 'Aurel', 'age': 7, 'candies': 3},
    {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# student2 = students[1]
# print (student2 ['name'])
#
# for student in students:
#     print(student['age'])
#
# total = 0
# for student in students:
#     if student['age'] < 10:
#         total += student['candies']
#
# print(total)

def get_all_candies_of_under_10(input):
    total = 0
    for student in input:
        if student['age'] < 10:
            total += student['candies']

    return(total)

print (get_all_candies_of_under_10(students))
