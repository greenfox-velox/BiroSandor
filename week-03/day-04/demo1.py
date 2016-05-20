def create_palindrom(input):
    output = ''
    for i in range((len(input) - 1), -1, -1):
        output += input[i]
        summ = input + output
    return summ

    # print(input + input[::-1)

print (create_palindrom('pear'))
