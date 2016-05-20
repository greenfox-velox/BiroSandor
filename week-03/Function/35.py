 #create a function that returns it's input factorial

number = 5


# x = 1
#
# while x <= number:
#     faktor *= x
#     x += 1
# print(faktor)


# for i in range(1, number + 1):
#     faktor *= i
# print(faktor)


def fakt(input):
    faktor = 1
    for i in range(1, input + 1):
        faktor *= i
    return faktor


print(fakt(number))
