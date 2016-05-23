# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    output = ''
    for i in result:
        temp = i.rstrip()
        temp = temp[::-1]
        temp = temp + '\n'
        output += temp

    f.close()

    return output
