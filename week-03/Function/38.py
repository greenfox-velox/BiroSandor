numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)

def minimal(input):
    min = input[0]
    for i in input:
        if i < min:
            min = i
    return min

print (minimal(numbers))
