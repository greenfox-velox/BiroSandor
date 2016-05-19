# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():

    def __init__(self):
        self.list = []

    def size(self):
        element = 0
        for i in self.list:
            element += 1
        return element
    def push(self, element):
        self.list += [element]

    def pop(self):
        # new_list = []
        #
        # for i in range(0, 2):
        #     last_element = self.list[-1]
        #     new_list += [self.list[i]]
        #
        # new_list = self.list
        # return last_element
        last_element = self.list[-1]
        self.list = self.list[0:-1]
        return last_element

item = Stack()
item.push('kutya')
item.push('2')
item.push('34')
item.push('7')
print (item.size())
print (item.list)
print (item.pop())
print (item.list)
