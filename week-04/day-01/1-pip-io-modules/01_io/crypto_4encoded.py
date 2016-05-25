# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    output = ''
    f.close()

    for character in result:
        if character in '\n ':
            output += character
        else:
            output += chr(ord(character)-1)
    return output
