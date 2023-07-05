'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''

from random import *
from time import *

weaponlist = [
  "20 piece chicken nuggets", "snowball", "bmx bike", "koala rabies", "cactus",
  "lightning mcqueen", "toothpick", "bath bomb", "rubber band",
  "washing machine", "1 dollar bill", "construction crane", "nerf gun",
  "AA battery"
]

zombieWeakness1 = weaponlist[randint(0, len(weaponlist) - 1)]
zombieWeakness2 = weaponlist[randint(0, len(weaponlist) - 1)]
zombieWeakness3 = weaponlist[randint(0, len(weaponlist) - 1)]
zombieWeakness4 = weaponlist[randint(0, len(weaponlist) - 1)]
userweapon = ""

#prompt
print(
  "After travelling far from your hometown on a quest to find treasure, you have stumbled into zombie territory! The locals warned you from going there but you proceeded ahead anyway."
)


def menu():
  choice1 = int(
    input("Actions:\n 1. Choose a weapon from the list\n 2. Use your own\n"))
  #check if it is 1 or 2
  if choice1 == 1 or choice1 == 2:
    choice2 = input("Ok, you chose " + str(choice1) + ", correct? (y/n)\n")
    #choice confirmation
    if choice2 == "y":
      if choice1 == 1:
        action1()
      elif choice1 == 2:
        action2()
    elif choice2 == "n":
      print("Ok, sending you back to the menu...")
      menu()
    else:
      print("Invalid input.")
      menu()
  else:
    print("Invalid input.")
    menu()


def action1():
  for i in range(len(weaponlist)):
    print(str(i + 1) + ". " + weaponlist[i])
  userweapon = int(input("Choose your weapon: "))
  choice3 = input("You chose " + weaponlist[userweapon - 1] +
                  ", correct? (y/n)\n")
  if choice3 == "y":
    if userweapon == zombieWeakness1 or userweapon == zombieWeakness2 or userweapon == zombieWeakness3 or userweapon == zombieWeakness4:
      print("You killed the zombie!")
    else:
      print("You died.")
    print("The zombie's weakness was " + zombieWeakness1 + ", " +
          zombieWeakness2 + ", " + zombieWeakness3 + ", and " +
          zombieWeakness3)
  elif choice3 == "n":
    print("Ok, choose again!")
    action1()
  else:
    print("Invalid input.")
    action1()


def action2():
  newweapon = input("Enter weapon: ")
  weaponlist.append(newweapon)
  #generate a new zomebieWeakness so it's more fair to the user
  zombieWeakness1 = weaponlist[randint(0, len(weaponlist) - 1)]
  zombieWeakness2 = weaponlist[randint(0, len(weaponlist) - 1)]
  zombieWeakness3 = weaponlist[randint(0, len(weaponlist) - 1)]
  zombieWeakness4 = weaponlist[randint(0, len(weaponlist) - 1)]
  if newweapon == zombieWeakness1 or newweapon == zombieWeakness2 or newweapon == zombieWeakness3 or newweapon == zombieWeakness4:
    print("You killed the zombie!")
  else:
    print("You died.")
  print("The zombie's weakness was " + zombieWeakness1 + ", " +
        zombieWeakness2 + ", " + zombieWeakness3 + ", and " + zombieWeakness3)


menu()
