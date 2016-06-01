import sys

class todo():
    def __init__(self):
        pass

    def usage(self):
        text = 'Python to do application\n========================\n\n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes an task\n-c   Completes an task'
        return text

    def list(self):
        f = open('list.txt')
        todo_list = f.readlines()
        f.close()
        output = ''
        j = 0
        if todo_list == []:
            no_todos = 'No todos for today! :)'
            return no_todos
        else:
            for i in todo_list:
                j += 1
                output += str(j) + ' - ' + i
            return output

    def main(self):
        if len(sys.argv) == 1:
            print(self.usage())
        elif sys.argv[1] == '-l':
            print(self.list())
        elif sys.argv[1] == '-a':
            if len(sys.argv) == 2:
                raise ValueError('Unable to add: No task is provided')
            else:
                f = open('list.txt', 'a')
                f.write(sys.argv[2] + '\n')
                f.close()
        elif sys.argv[1] == '-r':
            f = open('list.txt')
            remove_list = f.readlines()
            remove_list = remove_list[:(int(sys.argv[2]))-1] + remove_list[(int(sys.argv[2])):]
            f.close()
            remove_output = ''
            f = open('list.txt', 'w')
            for item in remove_list:
                remove_output += item
            f.write(remove_output)
            f.close()



first = todo()
try:
    first.main()
except ValueError as e:
    print(e)
