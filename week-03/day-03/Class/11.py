# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def tree_maker(input):
    for i in range(input + 1):
        print((input - i) * ' ' + i * '*'+ '*' + i * '*')
    for i in range(1,input + 1):
        print(i * ' ' + (input - i) * '*' + '*' +(input - i) * '*')

tree_maker(7)
