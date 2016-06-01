# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def lines_of_the_file(file_name):
    try:
        new = 0
        f = open(file_name)
        text = f.readlines()
        f.close()
        for i in range(len(text)):
            new += 1
        return new
    except FileNotFoundError:
        return 0

# print(lines_of_the_file(''))
print(lines_of_the_file('C:/Users/Sándor/Greenfox/BiroSandor/week-04/day-01/1-pip-io-modules/01_io/test.txt'))
