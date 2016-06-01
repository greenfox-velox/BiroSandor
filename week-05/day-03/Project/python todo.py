class todo():
    def __init__(self):
        pass

    def usage(self):
        text = 'Python to do application\n========================\n\n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes an task\n-c   Completes an task'
        return text


first = todo()
print(first.usage())
