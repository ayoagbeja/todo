FILEPATH = 'todos.txt'
def get_todos(filepath= FILEPATH):
    """"
    Read the text file and return the todos
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todo_args, filepath=FILEPATH):
    """"
    Writes a todo into a file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_args)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())