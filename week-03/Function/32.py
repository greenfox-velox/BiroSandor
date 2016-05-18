af = 123
# create a function that doubles it's input
# double af with it

# def double(input):
#     input *= 2
#     print(input)
#
# double(af)

def double(input):
    return input * 2

print (double(af))

def test(expected, actual):
    if expected == actual:
        print("check")
    else:
        print("jaj")

test(double(2), 4)
