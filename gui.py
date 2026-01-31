import functions
import FreeSimpleGUI as sg
import time

sg.theme("black")
clock = sg.Text('', key ='clock')
label= sg.Text('Type in a todo')
input_box = sg.InputText(tooltip = "Enter a to-do", key ="todo")

add_button = sg.Button( size= 2, mouseover_colors='Lightgreen', key= "Add",
                        tooltip = "Add Todo",image_source = "images/add.png")
list_box = sg.Listbox(values = functions.get_todos(), key ='todo list',
                      enable_events= True, size =[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button( size =6, image_source = "images/complete.png")

window = sg.Window('MY Todo App',
                   layout = [[clock],[label], [input_box, add_button],
                             [list_box, edit_button, complete_button]],
                   font= ('Helvetica', 20))
#event, values = window.read()
#todo_entry = values_dict.get('todo')

while True:
    event, values = window.read(timeout= 10) #this updates every 10ms
    window["clock"].update(value= time.strftime("%b %d, %Y %H:%M:%S"))
    print('1',event)
    print(2, values['todo'])
    print(3, values['todo list'])
    #window.read returns a tuple the button label and a dictionary containing the key and text

    match event:
        case "Add":
        #the event is the add button being clicked
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todo list'].update(values=todos)

        case "Edit":
            try:
            # the event is the edit button being clicked
                todo_to_edit = values['todo list'][0]
                new_todo= values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index]= new_todo + "\n"
                functions.write_todos(todos)
                window['todo list'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))


        case "Complete":
            try:
                completed_todo = values["todo list"][0]
                todos = functions.get_todos()
                todos.remove(completed_todo)
                functions.write_todos(todos)

                window['todo list'].update(values = todos)
                window['todo'].update(value = " ")

            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Exit":
            break

        case "todo list":
            window['todo'].update(value = values['todo list'][0])

        case sg.WIN_CLOSED:
            #this handles for when the close button is pressed
            break
window.close()