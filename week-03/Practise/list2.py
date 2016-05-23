# union([4,5,7], [4,1,7])
# expected output: [1,4,5,7]

numbers = [4, 5, 7]
numbers2 = [4, 1, 7]

new_list = numbers + numbers2
result = []
for i in new_list:
    if i not in result:
        result.append(i)
print(result)
