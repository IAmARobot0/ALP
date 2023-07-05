number = 7
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != number:
  print("Wrong! Guess again!")
  guess = int(input())
print("You guessed it!")

# Give the line number where iteration starts.
# Answer: line 4

# What does '!=' mean?
# Answer: not equal to

# How many variables are there in the code?
# Answer: 2, number and guess

# How can you tell which lines of code are inside the loop?
# Answer: lines 5 and 6

# How many times will the loop repeat?
# Answer: as many times until the user enters 7

# What has to happen to make the program run the last line of code?
# Answer: user must input 7 for the loop to stop and the program to continue

from math import *

secretnumber = 1
userguess = int(input("Guess what number I'm thinking of!\n"))
while userguess != secretnumber:
  difference = abs(userguess - secretnumber)
  if difference > 100:
    print("You are way off!")
  elif difference > 50:
    print("Your guess is pretty far away")
  elif difference > 25:
    print("You are getting really close but no...")
  elif difference > 10:
    print("SO CLOSE...")
  elif difference > 5:
    print("ALMOST THERE!")
  elif difference > 1:
    print("SUPER CLOSE!!")
  else:
    pass
  userguess = int(input("Wrong! Try again!\n"))
print("Congrats! You guessed correctly!")