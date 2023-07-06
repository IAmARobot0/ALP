# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)

from time import *
from random import *

name = input("Hello! I am a programmed chatbot. What is your name?\n")
sleep(1)
print("Hello, " + name + "!")
sleep(1)

#Question 1
feeling = input("On a scale of 1 to 10, how are you feeling today?\n")

sleep(1)
if int(feeling) > 8:
  print("Woohoo, " + name + "! That's awesome!")
elif int(feeling) > 6:
  print("That's pretty good, " + name + "!")
elif int(feeling) > 4:
  print("Ok, " + name + " it's not bad...")
elif int(feeling) > 2:
  print("Awww, hope your day gets better, " + name + ".")
elif int(feeling) > 0:
  print(name + ", maybe go take a break and go outside or something?")
else:
  feelinginput = input("Uhhh, are you ok, " + name + "? (y/n)\n")
  sleep(1)
  if feelinginput == "y":
    print("Ok, " + name + " maybe it's just one of those bad days")
  elif feelinginput == "n":
    print(
      "Dear " + name +
      ", help is available. Speak with someone today. Suicide and Crisis Lifeline: 988"
    )
  else:
    print("You are a bug hunter, " + name + "!")
sleep(1)

#Question 2
favFood = input("What is your favorite food?\n")
sleep(1)
print("Awesome, " + name + "! Maybe we can eat " + favFood + " next saturday!")
sleep(1)


def menu():
  choice = 0
  print("\n-----Menu-----")
  print("0. rock, paper, scissors")
  print("1. calculate area and perimeter (2d)")
  print("2. calculate volume and surface area (3d)")
  print("3. calculate restaurant tip")
  print("4. end")
  choice = int(input("What would you like to do?\n"))
  sleep(1)
  confirm(choice)


def confirm(choice):
  confirmation = input("you choose " + str(choice) + " correct? (y/n)\n")
  sleep(1)
  if confirmation == "y":
    if choice == 0:
      rps()
    elif choice == 1:
      aandp()
    elif choice == 2:
      vandsa()
    elif choice == 3:
      restauranttip()
    elif choice == 4:
      print("Ok, bye bye!")
      exit()
  elif confirmation == "n":
    menu()
  else:
    print("Sorry! Invalid input!")
    sleep(1)
    menu()


def rps():
  userinput = input(
    "Let's play rock, paper, scissors! Type r for rock, p for paper, and s for scissors!\n"
  )
  sleep(1)
  rps = ["r", "p", "s"]
  botinput = choices(rps, k=1)[0]
  if userinput == "r" or userinput == "p" or userinput == "s":
    if userinput == botinput:
      print("We tied!")
    elif userinput == "r" and botinput == "p":
      print(name + " loses. I choose paper.")
    elif userinput == "r" and botinput == "s":
      print(name + " wins! I choose scissors.")
    elif userinput == "p" and botinput == "r":
      print(name + " wins! I choose rock.")
    elif userinput == "p" and botinput == "s":
      print(name + " loses. I choose scissors.")
    elif userinput == "s" and botinput == "r":
      print(name + " loses. I choose rock.")
    elif userinput == "s" and botinput == "p":
      print(name + " wins! I choose paper.")
  else:
    print("Oops! Invalid input, " + name + ".")
  sleep(1)
  menu()


def aandp():
  h = int(input("height: "))
  w = int(input("width: "))
  area = h * w
  perimeter = 2 * (h + w)
  print("Area: " + str(area) + " units squared")
  print("Perimeter: " + str(perimeter) + " units")
  sleep(1)
  menu()


def vandsa():
  h = int(input("height: "))
  w = int(input("width: "))
  l = int(input("length: "))
  volume = l * w * h
  surfaceArea = 2 * (l * w + w * h + l * h)
  print("Volume: " + str(volume) + " units cubed")
  print("Surface Area: " + str(surfaceArea) + " units squared")
  sleep(1)
  menu()


def restauranttip():
  price = int(input("Enter price of meal: "))
  tip = price * 0.2
  total = price + tip
  print("Meal: " + str(price))
  print("Tip: " + str(tip))
  print("Total: " + str(total))
  sleep(1)
  menu()


menu()
