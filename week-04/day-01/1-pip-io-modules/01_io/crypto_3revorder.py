# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    temp = result[::-1]
    output = "".join(temp)
    f.close()
    return output
