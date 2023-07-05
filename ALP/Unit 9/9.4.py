import tkinter as tk
from tkinter import StringVar, ttk
from time import *
from random import *

userinput = ""
i = 0
datalist = []

root = tk.Tk()
w = root.winfo_height
root.geometry("400x200")
root.title("Calculator")

dialogue = ""
title = tk.Label(root, text=dialogue, compound="center", font=("Arial 20"))
title.grid(row=0, column=0, sticky="n")


def getnum1(i):
  dialogue = "Enter number 1:"
  title.config(text=dialogue)
  title.update()
  print(i)
  EnterButton.wait_variable(tk.StringVar())
  nextstep(i)


def getnum2(i):
  dialogue = "Enter number 1:"
  title.config(text=dialogue)
  title.update()
  print(i)
  EnterButton.wait_variable(tk.StringVar())
  nextstep(i)


def keep_data(newnumber):
  datalist.append(newnumber)
  print(datalist)


def get_data():
  if i == 0:
    num1 = entry.get()
    keep_data(num1)
  elif i == 1:
    num2 = entry.get()
    keep_data(num2)

  else:
    userinput = entry.get()
  entry.delete(0, tk.END)


evar = tk.StringVar()
entry = tk.Entry(root, textvariable=evar, width=30)
evar.set("")
entry.grid(row=1, column=0, sticky="n")
entry.focus()

EnterButton = tk.Button(root, text="Enter", command=get_data)
EnterButton.grid(row=2, column=0, sticky="n")


def next_question(i):
  if i == 0:
    getnum1(i)
  elif i == 1:
    userinput = ""
    getnum2(i)
  elif i == 2:
    response2()
  elif i == 3:
    userinput = ""
    question3()
  elif i == 4:
    response3()
  elif i == 5:
    userinput = ""
    question4()
  elif i == 6:
    response4()
  elif i == 7:
    userinput = ""
    question5()
  elif i == 8:
    response5()
  elif i == 9:
    userinput = ""
    question6()
  elif i == 10:
    response6()
  elif i == 11:
    userinput = ""
    question7()
  elif i == 12:
    response7()
  elif i == 13:
    userinput = ""
    question8()
  elif i == 14:
    response8()
  elif i == 15:
    question9()
  elif i == 16:
    response9()
  elif i == 17:
    goodbye()


def nextstep(i):
  i = i + 1
  next_question(i)


next_question(i)
'''

def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


def menu(n1, n2):
  print("-----MENU-----")
  print("1. add\n2. subtract\n3. multiply\n4. divide")
  userchoice = int(input("What would you like to do?\n"))
  if userchoice == 1:
    print("The sum is " + str(add(n1, n2)))
  elif userchoice == 2:
    print("The difference is " + str(subtract(n1, n2)))
  elif userchoice == 3:
    print("The product is " + str(multiply(n1, n2)))
  elif userchoice == 4:
    print("The quotient is " + str(divide(n1, n2)))
  else:
    print("Invalid input. Try again")
    menu(n1, n2)
  menu(n1, n2)


n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
menu(n1, n2)
'''
