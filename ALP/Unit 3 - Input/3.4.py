'''
Chat-Bot Challenge

Lots of websites use chat bots to interact with their customers.  These chat bots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the user their name and store it in a variable.
2. Greet the user by name.
3. Ask the user three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, using the 5. user’s name in the response.
5. Output a summary of all of the user’s answers in a single sentence.

'''

from time import *
from random import *
name = input("Hello! I am a programmed chatbot. What is your name?\n")
sleep(1)
print("Hello, " + name + "!")
sleep(1)

#Question 1
feeling = input("On a scale of 1 to 10, how are you feeling today?\n")

sleep(1)
if int(feeling)>8:
  print("Woohoo, " + name + "! That's awesome!")
elif int(feeling)>6:
  print("That's pretty good, " + name + "!")
elif int(feeling)>4:
  print("Ok, " + name + " it's not bad...")
elif int(feeling)>2:
  print("Awww, hope your day gets better, " + name + ".")
elif int(feeling)>0:
  print(name + ", maybe go take a break and go outside or something?")
else:
  feelinginput = input("Uhhh, are you ok, " + name + "? (y/n)\n")
  sleep(1)
  if feelinginput == "y":
    print("Ok, " + name + " maybe it's just one of those bad days")
  elif feelinginput == "n":
    print("Dear " + name + ", help is available. Speak with someone today. Suicide and Crisis Lifeline: 988")
  else:
    print("You are a bug hunter, " + name + "!")
sleep(1)

#Question 2
favFood = input("What is your favorite food?\n")
sleep(1)
print("Awesome, " + name + "! Maybe we can eat " + favFood + " next saturday!")
sleep(1)

#Question 3
playagain = "y"
while playagain == "y":
  userinput = input("Let's play rock, paper, scissors! Type r for rock, p for paper, and s for scissors!\n")
  sleep(1)
  rps = ["r", "p", "s"]
  botinput = choices(rps, k=1)[0]
  if userinput == "r" or userinput == "p" or userinput == "s":
    if userinput == botinput:
      print("We tied!")
    elif userinput == "r" and botinput == "p":
      print(name + " loses. I choose paper.")
    elif userinput == "r" and botinput =="s":
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
  playagain = input("Want to play again? (y/n)\n")
  sleep(1)
  if playagain == "y":
    print("Yay! I would love to play " + name + " again!")
  elif playagain == "n":
    print("Ok, we can always play again some other time, " + name + ".")
  else:
    print("Ummm, I'll take that as a no, " + name + ".")
sleep(1)
print("I have to go now. Bye bye " + name + "!")