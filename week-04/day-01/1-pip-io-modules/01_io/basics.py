# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    f = open(file_name)
    result = f.read()
    f.close()
    return result

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    for i in range(number):
        result = f.readline()
    f.close()
    return result.rstrip()
#print(readline('texts/zen_of_python.txt', 1))

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    sentence = sentence.rstrip('.')
    result = str.split(sentence)
    return result


# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    result = " ".join(words) + '.'
    return result

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    result = []
    for i in range(len(string)):
        result.append(ord(string[i]))
    return result

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
    result = ''
    for i in char_codes:
        result += chr(i)
    return result
