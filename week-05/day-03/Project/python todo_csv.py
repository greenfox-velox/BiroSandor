import sys
import csv

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

    def add_new_task(self):
        if len(sys.argv) == 2:
            print ('Unable to add: No task is provided')
        else:
            f = open('list.txt', 'a')
            f.write(sys.argv[2] + '\n')
            f.close()

    def remove_task(self):
        try:
            f = open('list.txt')
            remove_list = f.readlines()
            f.close()
            remove_list = remove_list[:(int(sys.argv[2]))-1] + remove_list[(int(sys.argv[2])):]
            remove_output = ''
            f = open('list.txt', 'w')
            for item in remove_list:
                remove_output += item
            f.write(remove_output)
            f.close()
            f = open('list.txt')
            listed_txt = f.readlines()
            length_list = len(listed_txt)
            f.close()
            if int(sys.argv[2]) > length_list:
                print('Unable to remove: Index is out of bound')
        except ValueError:
            print('Unable to remove: Index is not a number')
        except IndexError:
            print('Unable to remove: No index is provided')

    def argument_error(self):
        if len(sys.argv) > 1:
            if sys.argv[1] != '-l' and sys.argv[1] != '-a' and sys.argv[1] != '-r' and sys.argv[1] != '-c':
                print('Unsupported argument')


    def main(self):
        if len(sys.argv) == 1:
            print(self.usage())
        elif sys.argv[1] == '-l':
            print(self.list())
        elif sys.argv[1] == '-a':
            self.add_new_task()
        elif sys.argv[1] == '-r':
            self.remove_task()



first = todo()
first.main()
first.argument_error()
