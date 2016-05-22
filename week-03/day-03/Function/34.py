numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def summa(input):
    total = 0
    for i in input:
        total += i
    return total

print(summa(numbers))
