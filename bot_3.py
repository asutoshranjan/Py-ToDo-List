# highly optimised to_do bot

print("Hello This is BOT#3 a python powered Bot")
print("I will manage all your todos..")
print(" ")
name = input("Enter your name : ")
print(" ")
print("You can enter 'exit' to exit and -r to check a task done")
print(" ")
todo = []

task = "Random"
n = 0
while task != "exit":
    task = input("Enter a task : ")
    if task == "-r" :
        rtask = input("Which task is done : ")
        if rtask in todo:
            todo.remove(rtask)
            print(rtask, "marked as done")
            n -=1
        else:
            print(rtask, "not found in you todo list..")
    elif task != "exit" :
        todo.append(task)
        n +=1
print(" ")
print(name, "you have "+str(n)+" tasks todo..")
print(" ")
for tasks in todo:
    print(tasks)