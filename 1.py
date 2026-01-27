#getting input and printing it

'''name = input("Can i have your name : ")

age = int(input("And age too : "))

print("Welcome",name,", so you are",age,"years old, OK ")'''

#Conditional statment

''' age = int(input("age : "))

if(age >= 18):
    print("vote")
elif(age <= 7):
    print("Under age ")
else:
    print("Not ligiable ") '''

#Conditional statment with Logical operators

'''age = int(input("age : "))
gender = input("M/F : ")

if(age <= 5):
    print("NO fee")
elif(age<=10 and gender == ("M" or"m") and gender == ("F" or "f")):
    print("fee is 150")
elif(age > 10 or gender == ("F" or "f")):
    print("fee is 200")'''

#sngle line if statement
'''age = int(input("age : "))
print("no fee") if (age <= 10)  else print("fee is 200")'''

#type conversion and type casting
# a is int and b is float but result will implicitly convert into float
# and it is called type convestion
'''a = 2
b = 3.45
sum =(a+b)
print(sum)'''

# we explicitly convert string a into integier that is why
# is called type casting

'''a = int("2")
b = 3

print (type(a))'''


#'len' is ude to calculate the length of a certain value
'''str1 = "jobn" 
str2 = "preet"
print(len(str1))'''


'''#positive slicing
name = "jobanrandhawa"
slice = name[0:4]
print(slice)

#negative slicing
name = "jobanrandhawa"

slice = name[-13:-8]# -13 to -8 is from j to r but -8 will not be cout so it will be till -7(n)
print(slice)'''


'''my_tup = ["C", "D", "A", "A", "B", "B", "A"]
my_tup.sort()
print(my_tup)'''

'''import random

print("ROCK, PAPER, SISSOR SHOOT!")

choose = ["ROCK", "PAPER", "SISSOR"]

opp = input("YOUR TURN : ").upper()

choosed = random.choice(choose)

print("YOU :", opp)
print("COMPUTER :", choosed)


if(opp == choosed):
    print("LETS TRY AGAIN :")
elif(
    opp == "ROCK" and choosed == "SISSOR" or 
    opp == "SISSOR" and choosed == "PAPER" or
    opp =="PAPER" and choosed == "ROCK"
    ):
    print("YOU WON**")
else:
    print("YOU LOST**")'''


'''null_dict = {}

maths = float(input("Enter the marks of Maths : "))
english = float(input("Enter the marks of English : "))
science = float(input("Enter the marks of Science: "))

null_dict.update({"maths" : maths, "english" : english, "science" : science})

print(null_dict)'''

'''i = 1
while i <= 100 :
    print(i)
    i = i + 3'''

#Add, View, Delete task in list

'''list = []

while True :
    print("\n1. Add tasks")
    print("2. View tasks")
    print("3. Delete task")
    print("4. exit")
    

    choice = input("\nWrite your choice : ")

    if choice == '1':
        task = input("Write task you want to add : ")
        list.append(task)
        print("Task has been added sucessfully")

    elif choice == '2':
        for i, el in enumerate(list, 1):
            print(i, ".", el)

    elif choice == '3':
        num = int(input("Which task you want to delete : "))
        list.pop(num - 1)
        print("task has been deleted sucessfully")

    elif choice == '4':
        break

print("You logged out")'''

import os

path = "C:\Users\Dell\OneDrive\Desktop"
path2 = "C:\Users\Dell\OneDrive\Desktop\JobanFloder"
print(os.path.join(path, path2))






        
    



    








 