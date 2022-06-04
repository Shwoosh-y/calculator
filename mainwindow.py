
import tkinter as tk


m1 = open("n1.txt", "w")
m1.write("0")
m1.close()

num1 = tk.Tk()
num1.title('Please enter the first number')


#Defining functions for the buttons
def ones():
    m1 = open("n1.txt", "a")
    m1.write('1')
    m1.close
    m1 = open("n1.txt", "a")
def twos():
    m1 = open("n1.txt", "a")
    m1.write('2')
    m1.close
    m1 = open("n1.txt", "a")

def threes():
    m1 = open("n1.txt", "a")
    m1.write('3')
    m1.close
    m1 = open("n1.txt", "a")

def fours():
    m1 = open("n1.txt", "a")
    m1.write('4')
    m1.close
    m1 = open("n1.txt", "a")

def fives():
    m1 = open("n1.txt", "a")
    m1.write('5')
    m1.close
    m1 = open("n1.txt", "a")

def sixs():
    m1 = open("n1.txt", "a")
    m1.write('6')
    m1.close
    m1 = open("n1.txt", "a")

def sevens():
    m1 = open("n1.txt", "a")
    m1.write('7')
    m1.close
    m1 = open("n1.txt", "a")

def eights():
    m1 = open("n1.txt", "a")
    m1.write('8')
    m1.close
    m1 = open("n1.txt", "a")

def nines():
    m1 = open("n1.txt", "a")
    m1.write('9')
    m1.close
    m1 = open("n1.txt", "a")

def zeros():
    m1 = open("n1.txt", "a")
    m1.write('0')
    m1.close
    m1 = open("n1.txt", "a")

def enters():
    m1.close
    num1.destroy()

#Creating the buttons
one = tk.Button(num1, text='1', width=4, height=2, command=ones)
one.pack(side=tk.LEFT, anchor=tk.NW)

two = tk.Button(num1, text='2', width=4, height=2, command=twos)
two.pack(side=tk.LEFT, anchor=tk.NW)

three = tk.Button(num1, text='3', width=4, height=2, command=threes)
three.pack(side=tk.LEFT, anchor=tk.NW)

four = tk.Button(num1, text='4', width=4, height=2, command=fours)
four.pack(side=tk.LEFT, anchor=tk.NW)

five = tk.Button(num1, text='5', width=4, height=2, command=fives)
five.pack(side=tk.LEFT, anchor=tk.NW)

six = tk.Button(num1, text='6', width=4, height=2, command=sixs)
six.pack(side=tk.LEFT, anchor=tk.NW)

seven = tk.Button(num1, text='7', width=4, height=2, command=sevens)
seven.pack(side=tk.LEFT, anchor=tk.NW)

eight = tk.Button(num1, text='8', width=4, height=2, command=eights)
eight.pack(side=tk.LEFT, anchor=tk.NW)

nine = tk.Button(num1, text='9', width=4, height=2, command=nines)
nine.pack(side=tk.LEFT, anchor=tk.NW)

zero = tk.Button(num1, text='0', width=4, height=2, command=zeros)
zero.pack(side=tk.LEFT, anchor=tk.NW)

enter = tk.Button(num1, text='Enter', width=8, height=2, command=enters)
enter.pack(side=tk.LEFT, anchor=tk.NW)

num1.mainloop()



oper = tk.Tk()
oper.title('Please choose the operation')



#defining functions for the buttons

def pluss():

    opera = open("operas.txt", "w")
    opera.write('+')
    opera.close
    oper.destroy()

def minuss():

    opera = open("operas.txt", "w")
    opera.write('-')
    opera.close
    oper.destroy()

def divides():

    opera = open("operas.txt", "w")
    opera.write('/')
    opera.close
    oper.destroy()

def multiplys():

    opera = open("operas.txt", "w")
    opera.write('*')
    opera.close
    oper.destroy()


#Creating the buttons
plus = tk.Button(oper, text='+', width=4, height=2, command=pluss)
plus.pack(side=tk.LEFT, anchor=tk.NW)

minus = tk.Button(oper, text='-', width=4, height=2, command=minuss)
minus.pack(side=tk.LEFT, anchor=tk.NW)

divide = tk.Button(oper, text='/', width=4, height=2, command=divides)
divide.pack(side=tk.LEFT, anchor=tk.NW)

multiply = tk.Button(oper, text='*', width=4, height=2, command=multiplys)
multiply.pack(side=tk.LEFT, anchor=tk.NW)

oper.mainloop()
















m2 = open("n2.txt", "w")
m2.write("0")
m2.close()

num2 = tk.Tk()
num2.title('Please enter the second number')


#Defining functions for the buttons
def ones():
    m2 = open("n2.txt", "a")
    m2.write('1')
    m2.close
    m2 = open("n2.txt", "a")
def twos():
    m2 = open("n2.txt", "a")
    m2.write('2')
    m2.close
    m2 = open("n2.txt", "a")

def threes():
    m2 = open("n2.txt", "a")
    m2.write('3')
    m2.close
    m2 = open("n2.txt", "a")

def fours():
    m2 = open("n2.txt", "a")
    m2.write('4')
    m2.close
    m2 = open("n2.txt", "a")

def fives():
    m2 = open("n2.txt", "a")
    m2.write('5')
    m2.close
    m2 = open("n2.txt", "a")

def sixs():
    m2 = open("n2.txt", "a")
    m2.write('6')
    m2.close
    m2 = open("n2.txt", "a")

def sevens():
    m2 = open("n2.txt", "a")
    m2.write('7')
    m2.close
    m2 = open("n2.txt", "a")

def eights():
    m2 = open("n2.txt", "a")
    m2.write('8')
    m2.close
    m2 = open("n2.txt", "a")

def nines():
    m2 = open("n2.txt", "a")
    m2.write('9')
    m2.close
    m2 = open("n2.txt", "a")

def zeros():
    m2 = open("n2.txt", "a")
    m2.write('0')
    m2.close
    m2 = open("n2.txt", "a")

def enters():
    m2.close
    num2.destroy()

#Creating the buttons
one = tk.Button(num2, text='1', width=4, height=2, command=ones)
one.pack(side=tk.LEFT, anchor=tk.NW)

two = tk.Button(num2, text='2', width=4, height=2, command=twos)
two.pack(side=tk.LEFT, anchor=tk.NW)

three = tk.Button(num2, text='3', width=4, height=2, command=threes)
three.pack(side=tk.LEFT, anchor=tk.NW)

four = tk.Button(num2, text='4', width=4, height=2, command=fours)
four.pack(side=tk.LEFT, anchor=tk.NW)

five = tk.Button(num2, text='5', width=4, height=2, command=fives)
five.pack(side=tk.LEFT, anchor=tk.NW)

six = tk.Button(num2, text='6', width=4, height=2, command=sixs)
six.pack(side=tk.LEFT, anchor=tk.NW)

seven = tk.Button(num2, text='7', width=4, height=2, command=sevens)
seven.pack(side=tk.LEFT, anchor=tk.NW)

eight = tk.Button(num2, text='8', width=4, height=2, command=eights)
eight.pack(side=tk.LEFT, anchor=tk.NW)

nine = tk.Button(num2, text='9', width=4, height=2, command=nines)
nine.pack(side=tk.LEFT, anchor=tk.NW)

zero = tk.Button(num2, text='0', width=4, height=2, command=zeros)
zero.pack(side=tk.LEFT, anchor=tk.NW)

enter = tk.Button(num2, text='Enter', width=8, height=2, command=enters)
enter.pack(side=tk.LEFT, anchor=tk.NW)

num2.mainloop()







import os


os.system("cls")

n1 = "0"
n2 = "0"

#opening and reading files

m1 = open("./n1.txt")
opera = open("./operas.txt")
m2 = open("./n2.txt")

n1 = m1.read()
op = opera.read()
n2 = m2.read()

m1.close
opera.close
m2.close







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

resu =  tk.Tk()
resu.title('The Result is')
res = tk.Label(resu, text=(str(result)))
res.pack()
resu.mainloop()
