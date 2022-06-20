todo = []
name = input("Enter your name :")

print("Hi I am you personal todo bot ;)")
print(" ")
print("To exit in between type 'exit'")
print(" ")

task = input("Enter a task to do : ")
i = 0
if task != "exit" :
    todo.append(task)
    print(todo[i], "Added to your todo")
else:
    print("No To do :)")

while task != "exit" :
    task = input("Enter a task to do : ")
    todo.append(task)
    i +=1
    if task != "exit":
        print(todo[i], "Added to your todo")
    
print(" ")
print(i, "tasks to do ", name)
print(" ")
for c in range(i):
    print(todo[c])
