# create a function that takes a list and returns a new list that is reversed
numbers = [4, 5, 6, 7, 8, 9, 10]
def list_reverser(input):
    new_list = input[::-1]
    return new_list

print(list_reverser(numbers))
