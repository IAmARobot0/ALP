import tkinter as tk
from tkinter import StringVar, ttk
from time import *
from random import *

userinput = ""
i = 0
num1 = 1
num2 = 1
datalist = []

root = tk.Tk()
w = root.winfo_height
root.geometry("400x200")
root.title("Calculator")

dialogue = ""
title = tk.Label(root, text=dialogue, compound="center", font=("Arial 20"))
title.grid(row=0, column=0, sticky="n")

evar = tk.StringVar()
entry = tk.Entry(root, textvariable=evar, width=30)
evar.set("")
entry.grid(row=1, column=0, sticky="n")
entry.focus()





def get_data(i, datalist): #needs nextquestion and entry
  if i == 0:#displays prompt for num1
    i = i + 1# now i = 1
    dialogue = "Enter number 1:"
    title.config(text=dialogue)
    title.update()
    print(i)
    EnterButton.wait_variable(tk.StringVar())

  elif i == 1:#collects num1 and displays prompt for num2
    i = i + 1# now i = 2
    num1 = entry.get()
    datalist.append(num1)
    print(datalist)
    entry.delete(0,tk.END)
    dialogue = "Enter number 2:"
    title.config(text=dialogue)
    title.update()
    print(i)
    EnterButton.wait_variable(tk.StringVar())

  elif i == 2:
    num2 = entry.get()
    datalist.append(num2)
    print(datalist)
    entry.delete(0,tk.END)
    i = i + 1
    print("done")
  else:
    userinput = entry.get()
  entry.delete(0, tk.END)




EnterButton = tk.Button(root, text="Enter", command=get_data(i, datalist)) #needs getdata
EnterButton.grid(row=2, column=0, sticky="n")





root.mainloop()
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
