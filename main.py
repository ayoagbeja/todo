from functions import get_todos, write_todos
while True:
    user_action = input("Enter display, add, complete, edit or exit:").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = get_todos()
        #add to the todos
        todos.append(todo)

        #add the todo to the file
        write_todos( todo_args = todos, filepath ='todos.txt')

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            index = number - 1
            todos= get_todos()

            if index < len(todos):
                new_todo = input("What would you like to do instead?") + "\n"
                todos[index] = new_todo

                write_todos('todos.txt', todos)
            else:
                print("That todo does not exist.")

        except ValueError:
            print("Your command is invalid")
            continue

    elif  user_action.startswith("display") or user_action.startswith("show"):
        todos= get_todos()

        new_todos = []
        new_todos = [i.strip('\n') for i in todos]
       # for i in content:
        #    new_todos.append(i.strip('\n'))
        #print(new_todos)

        for i, j in enumerate(new_todos):
            row = f'{i +1}-{j}'
            print(row)

    elif  user_action.startswith("complete"):
        try:
            number = int(input("What number of todo would you like to complete?"))
            no_index = number-1

            todos = get_todos()

            if no_index in range(len(todos)):
                todo_removed = todos[no_index]
                todos.pop(no_index)

                write_todos('todos.txt', todos)
                print(f'Todo {todo_removed.strip("\n")} has been removed')

            else:
                print("The number is not in range")

        except IndexError:
            print("There is no todo with that number")
            continue
    elif user_action.startswith("exit"):
        print("Bye")
        break