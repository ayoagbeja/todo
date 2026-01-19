import functions
import FreeSimpleGUI as sg

label= sg.Text('Type in a todo')
input_box = sg.InputText(tooltip = "Enter a to-do", key ="todo")
add_button = sg.Button("Add")

edit_button = sg.Button("Edit")

window = sg.Window('MY Todo App',
                   layout = [[label], [input_box, add_button]],
                   font= ('Helvetica', 20))
event, values = window.read()
#todo_entry = values_dict.get('todo')

while True:
    event, values = window.read()
    #window.read returns a tuple the button label and a dictionary containing the key and text
    print(event)
    print(values)
    #print(todo_entry)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            #this handles for when the close button is pressed
            break
window.close()