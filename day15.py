#Print even numbers between 1 and 10
for i in range(1,11):
    if i %2== 0:
        print(i)

# Print numbers from 1 to 5 using a for loop
for i in range(1,6):
    print(i)

#Print multiplication table of a number
number = int(input("enter a number :"))
for num in range(1,11):
    print(f"{number} x {num} = {number * num}")

   #Print all characters of a string
    string = input("enter a string : ")
    for i in range(len(string)):
        print(string[i])

#nested loops
c = input ("enter a character : ")
for i in range(1,6):
    for j in range(1,6):
        print(c, end = " ")
        print()
