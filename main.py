import os


os.system("cls")

n1 = "0"
n2 = "0"

#Requesting user input
n1 = input("Please enter the first number: ")
op = input("Please enter the operation you want to perform (Supported is: + - * /): ")
n2 = input("Please enter the second number: ")
#Check for empty strings

if(n1 == ""):
    n1 = "0"
if(n2 == ""):
    n2 = 0



#Calculating
if(op == "+"):
    result = float(n1) + float(n2)

if(op == "-"):
    result = float(n1) - float(n2)

if(op == "*"):
    result = float(n1) * float(n2)

if(op == "/"):
    result = float(n1) / float(n2)





print(result)