names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def short(input):
    shortest = input[0]
    for i in input:
        if len(i) < len(shortest):
            shortest = i
    return shortest

print(short(names))
