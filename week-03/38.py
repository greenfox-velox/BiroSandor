# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

#1
# a = 0
# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#     i += 1



for i in range(0, 101):
    #if i % 15 == 0:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fuzz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)


for i in range(0, 101):
    #if i % 15 == 0:
    printable = ""
    if i % 3 == 0:
        printable = "Fizz"
    if i % 5 == 0:
        print("Fuzz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)
