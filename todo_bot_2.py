user_input = 'random'
data = []

def show_menu():
    print("")
    print("***  Menu  ***")
    print("1. add an item to todo")
    print("2. mark as done")
    print("3. all todo items")
    print("4. exit")

while user_input != "4":
    show_menu()
    user_input = input("Enter your choice : ")

    if user_input == "1":
        item = input("What is to be done ? ")
        data.append(item)
        print(item, "Added ToDo")
    elif user_input == "2":
        item = input("What is done? ")
        if item in data:
            data.remove(item)
            print(item, "Marked as done and removed from ToDo")
        else:
            print(item, "is no there in your todo list")
    elif user_input == "3":
        print(" ")
        print("Your ToDo List :")
        for task in data:
            print(task)
    elif user_input == "4":
        print("Goodbye..")
    else:
        print("Please enter only from 1,2,3,4 as options")