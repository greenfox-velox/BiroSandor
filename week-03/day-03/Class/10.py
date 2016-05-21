# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

def tree_maker(input):
    for i in range(input + 1):
        print((input - i) * ' ' + i * '*'+ '*' + i * '*')
    

tree_maker(7)
