aa = [1, 2, 3]
out = 0

lenaa = len(aa)

if lenaa == 0:
    out = -1
elif lenaa == 1:
    out = 1
elif lenaa == 2:
    out = 2
else:
    out = 10


print(out)

# if the aa list contains one element set the out to 1
# if the aa list contains two element set the out to 2
# if the aa list contains more than 2 set the out to 10
# if the aa contains no elements it should set to -1
