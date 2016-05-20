def search_palindrome(input):
    output = ''
    result = []
    for i in range(len(input) + 1):
        for x in range(len(input) + 1):
            output = (input[i:x])
            if len(output) >= 3 and output == output[::-1]:
                result += [output]
    return result

print(search_palindrome('dog goat dad duck doodle never'))
