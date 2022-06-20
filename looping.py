#while loop

r = input("Enter the range : ")
i = 1
while i<= int(r) :
    print(i)
    i += 1

print(5*"*")

#extracing the digs

b = 23
n = 0

while b>0:
    print(b%10)
    b = int(b/10)