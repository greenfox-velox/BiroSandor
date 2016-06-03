import sys
import csv

class Todo:
    def __init__(self):
        try:
            self.todo_list = self.open_csv()
        except FileNotFoundError:
            pass


    def usage(self):
        text = 'Python to do application\n========================\n\n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes an task\n-c   Completes an task'
        return text

    def open_csv(self):
        with open('list.csv', newline='') as f:
            todo_list = list(csv.reader(f, delimiter=';'))
        return todo_list

    # def open_csv_write(self):
    #     writeable_file = open('list.csv', 'w', newline='')
    #     data = csv.write(writeable_file)
    #     return writeable_file

    # def csv_write(self):
    #     with open('list.csv', 'w' ,newline='') as f:
    #         self.todo_list = list(csv.reader(f))
    #     return self.todo_list

    def list(self):
            output = ''
            j = 0
            if len(self.todo_list) == 0:
                no_todos = 'No todos for today! :)'
                return no_todos
            else:
                for i in self.todo_list:
                    j += 1
                    output += str(j) + ' - ' + str(i[0])+ '\n'
                return output

    def add_new_task(self, task):
        if len(sys.argv) == 2:
            print ('Unable to add: No task is provided')
        else:
            f = open('list.csv', 'a')
            f.write('False;' + task + '\n')
            f.close()



    def remove_task(self):
        try:
            f = open('list.csv')
            remove_list = f.readlines()
            f.close()
            remove_list = remove_list[:(int(sys.argv[2]))-1] + remove_list[(int(sys.argv[2])):]
            remove_output = ''
            f = open('list.csv', 'w')

            for item in remove_list:
                remove_output += item
            f.write(remove_output)
            f.close()
            f = open('list.csv')
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
            self.add_new_task(sys.argv[2])
        elif sys.argv[1] == '-r':
            self.remove_task()


first = Todo()
first.main()
first.argument_error()
