bubble_sort=[3,9,4,5,2,1]

for i in range(len(bubble_sort)):
    for x in range(len(bubble_sort)-1):
        if bubble_sort[x] > bubble_sort[x+1]:
            bubble_sort[x], bubble_sort[x+1] = bubble_sort[x+1], bubble_sort[x]
    print(bubble_sort)
