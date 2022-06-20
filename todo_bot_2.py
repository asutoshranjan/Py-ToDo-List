user_input = 'random'

def show_menu():
    print("")
    print("***  Menu  ***")
    print("1. add an item to todo")
    print("1. mark as do")
    print("1. all todo items")
    print("4. exit")

while user_input != "4":
    show_menu()
    user_input = input("Enter your choice : ")

    if user_input == "1":
        print("Add an item")
    elif user_input == "2":
        print("Mark as done")
    elif user_input == "3":
        print("view the todo items")
    elif user_input == "4":
        print("Goodbye..")
    else:
        print("Please enter only from 1,2,3,4 as options")