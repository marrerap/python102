todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

# for def examples
def print_todos():
    print("--------Todo's--------")
    
    count = 1
    for todo in todos:
        print(f'{count}: {todo}')
        count += 1

while True:
    print(''' 
    CHoose an option:

    1. Print Todos
    2. Add Todos
    3. Remove Todo
    0. Quit
    ''')
    user_choice = input('')

    if user_choice == "1":
        #print current todos
        print_todos

        #count = 1           moved to the function above
        # for todo in todos:
        #     print(f'{count}: {todo}')
        #     count += 1
    
    elif user_choice == "2":
        #add new item
        new_item = input('What do you want to add? ')
        todos.append(new_item)

    elif user_choice == "3":
        # delete a todo
        index = 0
        for todo in todos:
            print(f'{index}: {todo}')
            index += 1
        # the input has to be an integer so that del can work correctly
        delete_index = int(input('Which item would you like to delete? '))
        del todos[delete_index]
       

    elif user_choice == '0':
        #end the program
        app_is_open = False
