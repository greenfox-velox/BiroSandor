
# Adds a and b, returns as result
def add(a, b):
    return a+b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b:
        return a
    elif c > b:
        return c
    else:
        return b

# Returns the median value of a list given as param
def median(pool):
    # return pool[int((len(pool) - 1) / 2)]
    median = sorted(pool)
    if len(median) % 2 == 0:
        return (median[int(len(median)/2)-1] + median[(int(len(median)/2))])//2
    else:
        return median[int((len(median)-1)//2)]

# Returns true if the param is a vovel
def is_vovel(char):
    return char in 'aáeéiíoóöőuüűú'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
