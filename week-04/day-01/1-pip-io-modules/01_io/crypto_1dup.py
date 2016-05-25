# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    output = ''
    for  i in f:
        for x in range(0, len(i), 2):
            output += i[x]
    f.close()
    return output

print(decrypt('texts/duplicated_chars.txt'))
